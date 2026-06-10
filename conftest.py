import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

BASE_URL = os.getenv("CC_BASE_URL", "https://qc.care-connect.health")
USERNAME = os.getenv("CC_USERNAME", "careconnect@neorx.co")
PASSWORD = os.getenv("CC_PASSWORD", "")


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        yield context
        browser.close()


@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def logged_in_page(page):
    page.goto(BASE_URL + "/login")
    page.wait_for_load_state("networkidle")
    email_input = page.locator("input[type='email'], input[name='email'], input[placeholder*='mail' i]").first
    password_input = page.locator("input[type='password']").first
    email_input.fill(USERNAME)
    password_input.fill(PASSWORD)
    login_btn = page.locator("button[type='submit'], button:has-text('Login'), button:has-text('Sign In')").first
    login_btn.click()
    page.wait_for_url("**/dashboard**", timeout=15000)
    yield page


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def credentials():
    return {"username": USERNAME, "password": PASSWORD}


def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: quick smoke tests")
    config.addinivalue_line("markers", "regression: full regression tests")
    config.addinivalue_line("markers", "negative: negative/error path tests")
    config.addinivalue_line("markers", "ui: UI/visual tests")
