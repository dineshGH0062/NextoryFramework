from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegisterEmailPage:
    def __init__(self,driver):
        self.driver=driver
    def wait_for_home_page_to_load(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_email_textbox()))


    def get_email_textbox(self):
        try:
            element=self.driver.find_element_by_xpath("//input[@name='email']")
            return element
        except:
            return None


    def get_comfirm_email_textbox(self):
        try:
            element=self.driver.find_element_by_xpath("//input[@name='confirmemail']")
            return element
        except:
            return None


    def get_marketing_email_textbox(self):
        try:
            element=self.driver.find_element_by_xpath("//div[@class='checkbox']")
            return element
        except:
            return None


    def get_passowrd_textbox(self):
        try:
            element=self.driver.find_element_by_xpath("//input[@name='password']")
            return element
        except:
            return None

    def get_continue_button(self):
        try:
            element=self.driver.find_element_by_xpath("//button[contains(@class,'btn btn--primary btn--arrow')]")
            return element
        except:
            return None