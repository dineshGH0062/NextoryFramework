from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PaymentSelectionPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_home_page_to_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(self.get_adyen_payment()))

    def get_adyen_payment(self):
        try:
            element = self.driver.find_element_by_xpath("//div[@class='iconButton__label']")
            return element
        except:
            return None