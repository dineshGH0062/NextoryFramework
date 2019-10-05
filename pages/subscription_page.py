from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ChooseSubscriptionPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_home_page_to_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(self.get_guld_subscription_checkbox()))

    def get_guld_subscription_checkbox(self):
        try:
            element = self.driver.find_element_by_xpath("//div[@class='checkbox checkbox--active']")
            return element
        except:
            return None
    def get_seilver_subscription_checkbox(self):
        try:
            element = self.driver.find_element_by_xpath("//div[@class='subscriptionTable__name subscriptionTable__name--active']")
            return element
        except:
            return None


    def get_select_family_subscription(self):
        try:
            element=self.driver.find_element_by_xpath("(//div[@class='checkbox'])[2]")
            return element
        except:
            return None

    def get_continue_button(self):
        try:
            element = self.driver.find_element_by_xpath("//a[@class='btn btn--primary btn--arrow']")
            return element
        except:
            return None