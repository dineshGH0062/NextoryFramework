from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class PaymentSuccessPage:
    def __init__(self,driver):
        self.driver=driver



    def wait_for_paymet_sucess_page_to_load(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_first_name_text()))

    def get_first_name_text(self):
        try:
            element=self.driver.find_element_by_name("firstName")
            return element
        except:
            return None


    def get_last_name_text(self):
        try:
            element=self.driver.find_element_by_name("lastName")
            return element
        except:
            return None

    def get_mobile_number(self):
        try:
            element=self.driver.find_element_by_name("phoneNumber")

            return element
        except:
            return None

    def get_continue_button(self):
        try:
            element=self.driver.find_element_by_xpath("//button[contains(@class,'btn btn--primary btn--arrow')]")
            return element
        except:
            return None

    def get_go_to_mittkonto_page(self):
        try:
            element=self.driver.find_element_by_xpath("//a[@class='btn btn--secondary']")
            return element
        except:
            return None
