from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert (self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"), "Login url is not found"

    def should_be_login_form(self):
        try:
            self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"
        except NoSuchElementException:
            assert False
        assert True

    def should_be_register_form(self):
        try:
            self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"
        except NoSuchElementException:
            assert False
        assert True
        
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_password_input.send_keys(password)
        time.sleep(1)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_btn.click()
