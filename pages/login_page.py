from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Incorrect Login URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_FIELD), "Login username field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), "Login password field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_ENTER_BUTTON), "Login button is not presented"
        

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL_FIELD), "Registration email field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_FIELD), "Registration password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_CONFIRM_PASSWORD_FIELD), "Registration confirm password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), "Registration button is not presented"