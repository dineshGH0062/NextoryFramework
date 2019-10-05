from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CardDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_card_page_to_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(self.get_adyen_card_number()))

    def get_adyen_card_number(self):
        try:
            element = self.driver.find_element_by_id("encryptedCardNumber")
            return element
        except:
            return None


    def get_card_expiry_date(self):
        try:
            element=self.driver.find_element_by_id("encryptedExpiryDate")
            return element
        except:
            return None

    def get_card_cvv_number(self):
        try:
            element=self.driver.find_element_by_id("encryptedSecurityCode")
            return element
        except:
            return None

    def get_payment_countinue_button(self):
        try:
            element=self.driver.find_element_by_xpath("//button[@class='btn btn--primary btn--arrow ']")
            return element
        except:
            return None
