from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ShowSubscriptionPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_home_page_to_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(self.get_subscription_stage_1_button()))

    def get_subscription_stage_1_button(self):
        try:
            element = self.driver.find_element_by_xpath("//a[@class='btn btn--primary btn--arrow']")
            return element
        except:
            return None

