from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class MittKontoPage:
    def __init__(self,driver):
        self.driver=driver

    def wait_for_mittkonto_page_to_load(self):
        wait=WebDriverWait(self.driver,30)
        wait=wait.until(expected_conditions.visibility_of(self.get_my_information_link()))


    def get_my_information_link(self):
        try:
           element= self.driver.find_element_by_xpath("(//div[@class='accountNavigation__item'])[1]")
           return element
        except:
            return None

    def get_my_subscription_details_link(self):
        try:
           element= self.driver.find_element_by_xpath("(//div[@class='accountNavigation__item'])[2]")
           return element
        except:
            return None
    def get_my_payemt_details_link(self):
        try:
           element= self.driver.find_element_by_xpath("(//div[@class='accountNavigation__item'])[3]")
           return element
        except:
            return None

    def get_my_offer_details_link(self):
        try:
           element= self.driver.find_element_by_xpath("(//div[@class='accountNavigation__item'])[4]")
           return element
        except:
            return None

    def get_my_order_history_link(self):
        try:
           element= self.driver.find_element_by_xpath("(//div[@class='accountNavigation__item'])[5]")
           return element
        except:
            return None

    def get_logout_button(self):
        try:
           element= self.driver.find_element_by_xpath("//button[@class='btn btn--secondary']")
           return element
        except:
            return None
