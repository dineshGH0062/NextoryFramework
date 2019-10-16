
import pytest
#import logging as log
from selenium.webdriver.common.keys import Keys

from pages.home_page import HomePage
from pages.stage_1_page import ShowSubscriptionPage
from pages.signup_email_page import RegisterEmailPage
from pages.stage_2_page import EmailPage
from pages.subscription_page import ChooseSubscriptionPage
from pages.user_details_page import MyDetailsPage
from pages.konto_page import MittKontoPage
from pages.thank_page import PaymentSuccessPage
from pages.payment_selection_page import PaymentSelectionPage
from pages.card_details_page import CardDetailsPage
from pages.family_subscription_page import FamilySubscriptionPage
from utils import utils as utils
import random
import string

#log.basicConfig()


@pytest.mark.usefixtures("test_setup")
class TestRegistration():
    def generate_email(prefix='test_py', domain='frescano.se'):
        random_part = ''.join(random.choice(string.ascii_uppercase + string.digits)
                              for _ in range(2))

        return prefix + random_part + '@' + domain

    email = generate_email()
    def test_homepage_button(self):
        driver = self.driver
        driver.get(utils.URL)
        home = HomePage(driver)
        home.wait_for_home_page_to_load()
        #log.info("Inside testing")
        home.get_free_for_14_days_button().click()

    def test_clickToShowSub(self):
        driver=self.driver
        steg1=ShowSubscriptionPage(driver)
        steg1.wait_for_home_page_to_load()
        steg1.get_subscription_stage_1_button().click()

    def test_chooseSub(self):
        driver=self.driver
        subs=ChooseSubscriptionPage(driver)
        subs.wait_for_home_page_to_load()
        subs.get_guld_subscription_checkbox()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # subs.get_seilver_subscription_checkbox()
        # subs.get_select_family_subscription()
        subs.get_continue_button().click()

    def test_clickTo_Email(self):
        driver=self.driver
        clicktoEmail=EmailPage(driver)
        clicktoEmail.wait_for_email_page_to_load()
        clicktoEmail.get_email_button().click()

    def test_registration_textbox(self):
        driver=self.driver
        signUp=RegisterEmailPage(driver)
        signUp.wait_for_home_page_to_load()
        signUp.get_email_textbox().send_keys(self.email)
        signUp.get_comfirm_email_textbox().send_keys(self.email)
        signUp.get_passowrd_textbox().send_keys("password")
        signUp.get_marketing_email_textbox().click()
        signUp.get_continue_button().click()


    def test_payment(self):
        driver=self.driver
        payment=PaymentSelectionPage(driver)
        payment.wait_for_home_page_to_load()
        payment.get_adyen_payment().click()

    def test_card_details(self):
        driver=self.driver
        cardDetails=CardDetailsPage(driver)
        #cardDetails.wait_for_card_page_to_load()
        driver.switch_to.frame(0)
        cardDetails.get_adyen_card_number().clear()
        cardDetails.get_adyen_card_number().send_keys(utils.CreditCard)
        driver.switch_to.default_content()
        driver.switch_to.frame(1)
        cardDetails.get_card_expiry_date().send_keys(utils.ExpiryDate)
        driver.switch_to.default_content()
        driver.switch_to.frame(2)
        cardDetails.get_card_cvv_number().send_keys(utils.CVV)
        driver.switch_to.default_content()
        #driver.execute_script("window.scrollTo(0, 200);")
        cardDetails.get_payment_countinue_button().click()

    def test_success_page(self):
        driver=self.driver
        userDetails=PaymentSuccessPage(driver)
        userDetails.wait_for_paymet_sucess_page_to_load()
        userDetails.get_first_name_text().send_keys(utils.FirstName)
        userDetails.get_last_name_text().send_keys(utils.LastName)
        userDetails.get_mobile_number().send_keys(utils.PhoneNumber)
        userDetails.get_continue_button().click()
        userDetails.get_go_to_mittkonto_page().click()

    def test_mittkont(self):
        driver=self.driver
        mittKonto=MittKontoPage(driver)
        mittKonto.wait_for_mittkonto_page_to_load()
        mittKonto.get_logout_button().click()




