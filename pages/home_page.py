from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_home_page_to_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(self.get_free_for_14_days_button()))



    def get_free_for_14_days_button(self):
        try:
            return self.driver.find_element_by_xpath("//a[@class='btn btn--primary']")
        except:
            return None

    def get_login_button(self):
        try:
            return self.driver.find_element_by_xpath("//a[@class='navigation__link'][contains(text(),'Log på')]")
        except:
            return None

    def get_camp_button(self):
        try:
            element = self.driver.find_element_by_xpath("//a[contains(text(),'Kampagnekode')]")
            return element
        except:
            return None

    def get_login_error_msg(self):
        try:
            return self.driver.find_element_by_xpath(
                "//span[text()='Username or Password is invalid. Please try again.']")
        except:
            return None


        def get_camp_button(self):
            try:
                element = self.driver.find_element_by_xpath("//a[contains(text(),'Kampagnekode')]")
                return element
            except:
                return None