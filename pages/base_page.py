"""Base Page Object - shared methods for all pages."""
from playwright.sync_api import Page
import logging
logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        logger.info(f"Navigating to: {url}")
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def get_title(self) -> str:
        return self.page.title()

    def get_current_url(self) -> str:
        return self.page.url

    def is_element_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def take_screenshot(self, name: str):
        import os
        os.makedirs("reports/screenshots", exist_ok=True)
        self.page.screenshot(path=f"reports/screenshots/{name}.png", full_page=True)
