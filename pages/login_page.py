"""Login Page Object Model for CareConnect."""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import logging
logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    USERNAME_INPUT  = 'input[placeholder="Enter your username"]'
    PASSWORD_INPUT  = 'input[placeholder="Enter your password"]'
    SHOW_HIDE_BTN   = 'button[type="button"]:near(input[type="password"])'
    LOGIN_BUTTON    = 'button[type="submit"]'
    RESET_PWD_LINK  = 'a[href="/side-forgot-pwd"]'
    AR_LANG_BUTTON  = 'button:has-text("العربية")'
    BRAND_LOGO      = 'img[alt="CareConnect Logo"]'
    ERROR_MESSAGE   = '[class*="error"], [class*="alert"], [role="alert"]'

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        from utils.test_data import LOGIN_URL
        self.navigate(LOGIN_URL)
        return self

    def enter_username(self, username: str):
        self.page.fill(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str):
        self.page.fill(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        self.page.click(self.LOGIN_BUTTON)
        self.page.wait_for_load_state("networkidle")
        return self

    def login(self, username: str, password: str):
        return self.enter_username(username).enter_password(password).click_login()

    def click_reset_password(self):
        self.page.click(self.RESET_PWD_LINK)
        self.page.wait_for_load_state("networkidle")
        return self

    def toggle_password_visibility(self):
        self.page.click(self.SHOW_HIDE_BTN)
        return self

    def get_username_value(self): return self.page.input_value(self.USERNAME_INPUT)
    def get_password_input_type(self): return self.page.get_attribute(self.PASSWORD_INPUT, "type")
    def get_error_message(self):
        try: return self.page.text_content(self.ERROR_MESSAGE)
        except: return ""
    def is_login_button_visible(self): return self.page.is_visible(self.LOGIN_BUTTON)
    def is_login_button_enabled(self): return self.page.is_enabled(self.LOGIN_BUTTON)
    def is_reset_password_link_visible(self): return self.page.is_visible(self.RESET_PWD_LINK)
    def is_logo_visible(self): return self.page.is_visible(self.BRAND_LOGO)
    def get_username_placeholder(self): return self.page.get_attribute(self.USERNAME_INPUT, "placeholder")
