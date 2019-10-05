from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class FamilySubscriptionPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_family_subscription_page_to_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(self.get_family2_selection_subscription()))

    def get_family2_selection_subscription(self):
        try:
            element = self.driver.find_element_by_xpath("//p[@class='amountPicker__heading'][contains(text(),'2')]")
            return element
        except:
            return None

    def get_family3_selection_subscription(self):
        try:
            element = self.driver.find_element_by_xpath("//p[@class='amountPicker__heading'][contains(text(),'2')]")
            return element
        except:
            return None
    def get_family4_selection_subscription(self):
        try:
            element = self.driver.find_element_by_xpath("//p[@class='amountPicker__heading'][contains(text(),'2')]")
            return element
        except:
            return None

    def get_continue_button(self):
        try:
            element = self.driver.find_element_by_xpath("//a[@class='btn btn--primary btn--arrow']")
            return element
        except:
            return None
