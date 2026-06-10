"""Dashboard Page Object Model for CareConnect."""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import logging
logger = logging.getLogger(__name__)

class DashboardPage(BasePage):
    LOGO                = 'img[alt="logo"]'
    SELECT_FACILITY_BTN = 'button:has-text("Select Facility")'
    LANG_TOGGLE         = 'li:has-text("العربية")'
    PROFILE_AVATAR      = 'button img[alt="Profile"]'
    NOTIFICATION_ICON   = 'li:nth-child(3) button'
    NAV_DASHBOARD       = 'a[href="/dashboard"]'
    NAV_USERS           = 'a[href="/user"]'
    NAV_ROLES           = 'a[href="/role"]'
    NAV_PATIENTS        = 'a[href="/patient-management/patient"]'
    NAV_VISITS          = 'a[href="/patient-management/visit"]'
    NAV_PRESCRIPTIONS   = 'a[href="/prescribe-management/prescriptions"]'
    NAV_DISPENSE        = 'a[href="/dispensing-management/dispensing"]'
    NAV_CLAIMS          = 'a[href="/claiming-management/claims"]'
    NAV_CDSS_CONFIG     = 'a[href="/cdss-management/configurations"]'
    NAV_FRAUD_CASES     = 'a[href="/fraud-management/fraud-cases"]'
    NAV_AUDIT_LOG       = 'a[href="/audit-log"]'
    NAV_SETTINGS        = 'a[href="/settings"]'
    USER_STATS_SHOW_MORE= 'button:has-text("Show More")'
    FOOTER_COPYRIGHT    = ':has-text("All rights reserved")'
    FOOTER_NEORX_LINK   = 'a[href="https://neorx.co/"]'

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        from utils.test_data import BASE_URL
        self.navigate(f"{BASE_URL}/dashboard")
        return self

    def click_nav_item(self, href: str):
        self.page.click(f'a[href="{href}"]')
        self.page.wait_for_load_state("networkidle")
        return self

    def is_sidebar_visible(self): return self.page.is_visible(self.NAV_DASHBOARD)
    def is_select_facility_visible(self): return self.page.is_visible(self.SELECT_FACILITY_BTN)
