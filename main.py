from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PropertyListing import PropertyListing
import time
import pandas as pd

if __name__ == "__main__":
    try:

        url_to_scrape = f'https://www.centris.ca/en/plexes~for-sale~montreal-ouest?view=Thumbnail&uc=6'
        webdriver_path = ''
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(webdriver_path)
        driver.get(url_to_scrape)
        
        links = list()
        last_page = False
        while not last_page:
            items = driver.find_elements_by_class_name('a-more-detail')
            page_links = [item.get_attribute('href') for item in items]
            links.extend(list(set(page_links)))
            
            if "inactive" in driver.find_element_by_class_name("next").get_attribute('class'):
                break
            driver.find_element_by_class_name('next').click()
            time.sleep(3)
        driver.close()
        ## Extracting Data
        property_list = list()
        [property_list.append(PropertyListing(link)) for link in links]
        [property.get_data() for property in property_list]

        ## Saving Data
        df = pd.DataFrame()
        for property in property_list:
            df = pd.concat([df, property.to_dataframe()])
        df.to_csv('result.csv')

    finally:
        driver.close()
