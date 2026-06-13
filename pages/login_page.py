import os
from pages.base_page import BasePage

BASE_URL = os.getenv("CC_BASE_URL", "https://qc.care-connect.health")


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = BASE_URL + "/login"

        # Correct locators from live inspection of the page
        self.email_input = "#username"
        self.password_input = "#password"
        self.login_button = "button[type='submit'], button:has-text('Login'), button:has-text('Sign In'), button:has-text('Log In')"
        self.error_message = ".error, .alert, [class*='error'], [class*='alert'], [class*='invalid']"

    def navigate(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")

    def enter_email(self, email):
        self.page.locator(self.email_input).fill(email)

    def enter_password(self, password):
        self.page.locator(self.password_input).fill(password)

    def click_login_button(self):
        self.page.locator(self.login_button).first.click()

    def login(self, email, password):
        self.navigate()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def is_email_field_visible(self):
        return self.page.locator(self.email_input).is_visible()

    def is_password_field_visible(self):
        return self.page.locator(self.password_input).is_visible()

    def is_login_button_visible(self):
        return self.page.locator(self.login_button).first.is_visible()

    def has_error_message(self):
        try:
            return self.page.locator(self.error_message).first.is_visible()
        except Exception:
            return False

    def get_email_value(self):
        return self.page.locator(self.email_input).input_value()

    def is_password_masked(self):
        field_type = self.page.locator(self.password_input).get_attribute("type")
        return field_type == "password"
