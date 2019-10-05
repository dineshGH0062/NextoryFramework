import pytest
from selenium.webdriver.common.keys import Keys
from pages.login_page import LoginPage
from utils import utils as utils
from pages.konto_page import MittKontoPage

@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_login_button(self):
        driver=self.driver
        driver.get(utils.URL)
        login=LoginPage(driver)
        login.wait_for_login_page_to_load()
        login.get_login_button().click()
        login.get_email_textbox().send_keys(utils.Email)
        login.get_password_textbox().send_keys(utils.Password)
        login.get_login_click_button().click()

    def test_mitt_konto(self):
        driver=self.driver
        konto=MittKontoPage(driver)
        konto.get_logout_button()

