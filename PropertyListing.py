from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd


class PropertyListing:
    def __init__(self, url):
        self.listing_url = url
        self.property_type = None
        self.listed_price = None
        self.listed_address = None
        self.building_style = None
        self.lot_area = None
        self.parking = None
        self.main_unit = None
        self.listed_potential_gross_revenue = None
        self.listed_walk_score = None
        self.number_of_units = None
        self.year_built = None   
        self.description = None

    def get_data(self):
        webdriver_path = ''
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(webdriver_path)
        driver.get(self.listing_url)
        try:
            self.property_type = driver.find_element_by_css_selector("span[data-id='PageTitle']").text
        except:
            pass
        try:
            self.listed_price = driver.find_element_by_id('BuyPrice').text
        except:
            pass
        try:
            self.listed_address = driver.find_element_by_css_selector("h2[itemprop='address']").text
        except:
            pass
        try:
            self.building_style = driver.find_element_by_xpath("//*[contains(text(), 'Building style')]/..").find_element_by_class_name('carac-value').text
        except:
            pass
        try:
            self.lot_area = driver.find_element_by_xpath("//*[contains(text(), 'Lot area')]/..").find_element_by_class_name('carac-value').text
        except:
            pass
        try:
            self.parking = driver.find_element_by_xpath("//*[contains(text(), 'Parking (total)')]/..").find_element_by_class_name('carac-value').text
        except:

            pass
        try:
            self.main_unit = driver.find_element_by_xpath("//*[contains(text(), 'Main unit')]/..").find_element_by_class_name('carac-value').text
        except:
            pass
        try:
            self.listed_potential_gross_revenue = driver.find_element_by_xpath("//*[contains(text(), 'Potential gross revenue')]/..").find_element_by_class_name('carac-value').text
        except:
            pass
        try:
            self.listed_walk_score = driver.find_element_by_class_name('walkscore').text
        except:
            pass
        try:
            self.number_of_units = driver.find_element_by_xpath("//*[@data-id='NbUniteFormatted']").text
        except:
            pass
        try:
            self.year_built = driver.find_element_by_xpath("//*[contains(text(), 'Year built')]/..").find_element_by_class_name('carac-value').text
        except:
            pass
        try:
            self.description = driver.find_element_by_css_selector("div[itemprop='description']").text
        except:
            pass

        driver.close()

    def to_dataframe(self):
        df = pd.DataFrame(self.__dict__, index=[0])
        return df


        
