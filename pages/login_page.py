from pages.base_page import BasePage
from utils.locators import LoginPageLocators

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.send_keys(LoginPageLocators.USERNAME_INPUT, username)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        
    def get_error_message(self):
        return self.get_text(LoginPageLocators.ERROR_MESSAGE)
