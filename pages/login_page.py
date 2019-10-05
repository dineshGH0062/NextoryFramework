from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    def wait_for_login_page_to_load(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_login_button()))


    def get_login_button(self):
        try:
            return self.driver.find_element_by_xpath("//a[@class='navigation__link'][contains(text(),'Log på')]")
        except:
            return None

    def get_email_textbox(self):
        try:
            return self.driver.find_element_by_xpath("//input[@name='email']")
        except:
            return None
    def get_password_textbox(self):
        try:
            return self.driver.find_element_by_xpath("//input[@type='password']")
        except:
            return None

    def get_login_click_button(self):
        try:
            return self.driver.find_element_by_xpath("//button[contains(@class,'btn btn--primary')]")
        except:
            return None