"""Visits Page Object Model for CareConnect."""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import logging
logger = logging.getLogger(__name__)

class VisitsPage(BasePage):
    FACILITY_MODAL_TITLE = 'text=Select Current Facility'
    FACILITY_WARNING     = 'text=You need to have a selected facility in order to access this page'
    VISITS_LIST_HEADING  = 'text=Visits List'
    ADD_VISIT_BTN        = 'button:has-text("Add")'
    SEARCH_KEYWORD_INPUT = 'input[placeholder="Search keyword"]'
    EXPORT_BTN           = 'button:has-text("Export")'
    VISIT_FORM_HEADING   = 'text=Visit Information'
    FORM_ADD_BTN         = 'button[type="submit"]:has-text("Add")'
    FORM_CANCEL_BTN      = 'button:has-text("Cancel")'
    REQUIRED_ERROR       = 'text=This field is required'

    def __init__(self, page: Page):
        super().__init__(page)

    def is_facility_modal_visible(self):
        return self.page.is_visible(self.FACILITY_MODAL_TITLE)

    def select_facility(self, facility_name: str):
        self.page.locator('.p-dropdown-trigger').first.click()
        self.page.wait_for_timeout(500)
        self.page.locator(f'.p-dropdown-item:has-text("{facility_name}")').click()
        self.page.wait_for_load_state("networkidle")
        return self

    def click_add_visit(self):
        self.page.click(self.ADD_VISIT_BTN)
        self.page.wait_for_load_state("networkidle")
        return self

    def select_patient(self, patient_name: str):
        self.page.locator('label:has-text("Patient ID") ~ div button').first.click()
        self.page.wait_for_timeout(400)
        self.page.locator('input[role="searchbox"]').first.fill(patient_name[:6])
        self.page.wait_for_timeout(800)
        self.page.locator(f'.p-dropdown-item:has-text("{patient_name}")').first.click()
        self.page.wait_for_timeout(300)
        return self

    def select_physician(self, physician_name: str):
        self.page.locator('label:has-text("Physician ID") ~ div button').first.click()
        self.page.wait_for_timeout(400)
        self.page.locator('input[role="searchbox"]').last.fill(physician_name[:7])
        self.page.wait_for_timeout(800)
        self.page.locator(f'.p-dropdown-item:has-text("{physician_name}")').click()
        self.page.wait_for_timeout(300)
        return self

    def select_encounter_type(self, encounter_type: str):
        self.page.locator('label:has-text("Encounter Type") ~ div button').first.click()
        self.page.wait_for_timeout(400)
        self.page.locator(f'.p-dropdown-item:has-text("{encounter_type}")').click()
        self.page.wait_for_timeout(300)
        return self

    def set_visit_date_today(self):
        self.page.locator('.p-calendar input').first.click()
        self.page.wait_for_timeout(500)
        self.page.locator('button:has-text("Today")').click()
        self.page.wait_for_timeout(300)
        return self

    def click_add_submit(self):
        self.page.locator(self.FORM_ADD_BTN).click()
        self.page.wait_for_load_state("networkidle")
        return self

    def click_cancel(self):
        self.page.locator(self.FORM_CANCEL_BTN).click()
        self.page.wait_for_load_state("networkidle")
        return self

    def is_facility_pre_filled(self, facility_name: str):
        return self.page.is_visible(f'text={facility_name}')
