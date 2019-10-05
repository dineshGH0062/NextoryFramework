from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class MyDetailsPage:
    def __inti__(self,driver):
        self.driver=driver


    def wail_for_my_details_page_to_load(self):
        wait=WebDriverWait(self.driver,30)
        wait=wait.until(expected_conditions.visibility_of)


    def get_adress_details(self):
        try:
            element=self.driver.find_element_by_name("//input[@name='address']")
            return element
        except:
            return None

    def get_zip_code(self):
        try:
            element=self.driver.find_element_by_name("zipCode")
            return element
        except:
            return None

    def get_city_name(self):
        try:
            element=self.driver.find_element_by_name("city")
            return element
        except:
            return None

    def get_save_button(self):
        try:
            element=self.driver.find_element_by_xpath("//button[contains(@class,'btn btn--primary')]")
            return element
        except:
            return None
