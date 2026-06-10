import pytest
from pages.login_page import LoginPage
from utils.test_data import TestData


@pytest.mark.smoke
class TestLoginSmoke:
    def test_login_page_loads(self, page, base_url):
        page.goto(base_url + "/login")
        page.wait_for_load_state("networkidle")
        assert page.url.endswith("/login") or "login" in page.url

    def test_login_form_visible(self, page, base_url):
        login = LoginPage(page)
        login.navigate()
        assert login.is_email_field_visible()
        assert login.is_password_field_visible()

    def test_successful_login(self, page, credentials, base_url):
        login = LoginPage(page)
        login.navigate()
        login.login(credentials["username"], credentials["password"])
        page.wait_for_url("**/dashboard**", timeout=15000)
        assert "dashboard" in page.url

    def test_login_button_visible(self, page, base_url):
        login = LoginPage(page)
        login.navigate()
        assert login.is_login_button_visible()


@pytest.mark.negative
class TestLoginNegative:
    def test_login_empty_credentials(self, page, base_url):
        login = LoginPage(page)
        login.navigate()
        login.click_login_button()
        assert "login" in page.url or login.has_error_message()

    def test_login_invalid_email(self, page, base_url):
        login = LoginPage(page)
        login.navigate()
        login.login("invalid@test.com", "wrongpass")
        page.wait_for_timeout(2000)
        assert "login" in page.url or login.has_error_message()

    def test_login_wrong_password(self, page, credentials, base_url):
        login = LoginPage(page)
        login.navigate()
        login.login(credentials["username"], "wrongpassword123")
        page.wait_for_timeout(2000)
        assert "login" in page.url or login.has_error_message()

    def test_login_empty_password(self, page, credentials, base_url):
        login = LoginPage(page)
        login.navigate()
        login.login(credentials["username"], "")
        page.wait_for_timeout(1000)
        assert "login" in page.url or login.has_error_message()


@pytest.mark.ui
class TestLoginUI:
    def test_page_title(self, page, base_url):
        page.goto(base_url + "/login")
        page.wait_for_load_state("domcontentloaded")
        title = page.title()
        assert len(title) > 0

    def test_email_field_accepts_input(self, page, base_url):
        login = LoginPage(page)
        login.navigate()
        login.enter_email("test@example.com")
        value = login.get_email_value()
        assert "test@example.com" in value

    def test_password_field_masked(self, page, base_url):
        login = LoginPage(page)
        login.navigate()
        assert login.is_password_masked()
