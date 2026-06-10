import pytest
import random
from datetime import datetime
from pages.visits_page import VisitsPage
from utils.test_data import TestData


@pytest.mark.smoke
class TestVisitsSmoke:
    def test_visits_page_loads(self, logged_in_page, base_url):
        logged_in_page.goto(base_url + "/patient-management/visit")
        logged_in_page.wait_for_load_state("networkidle")
        assert "visit" in logged_in_page.url.lower()

    def test_visits_list_visible(self, logged_in_page, base_url):
        visits = VisitsPage(logged_in_page)
        visits.navigate()
        assert visits.is_visits_list_visible()

    def test_add_visit_button_visible(self, logged_in_page, base_url):
        visits = VisitsPage(logged_in_page)
        visits.navigate()
        assert visits.is_add_button_visible()


@pytest.mark.regression
class TestAddVisit:
    def test_add_new_visit_form_opens(self, logged_in_page, base_url):
        visits = VisitsPage(logged_in_page)
        visits.navigate()
        visits.click_add_button()
        logged_in_page.wait_for_url("**/visit/new**", timeout=10000)
        assert "new" in logged_in_page.url

    def test_add_visit_with_required_fields(self, logged_in_page, base_url):
        today = datetime.now().strftime("%m/%d/%Y")
        encounter_type = random.choice(TestData.ENCOUNTER_TYPES)
        visits = VisitsPage(logged_in_page)
        visits.navigate()
        visits.click_add_button()
        visits.select_patient(TestData.PATIENT_NAME)
        visits.select_physician(TestData.PHYSICIAN_NAME)
        visits.select_encounter_type(encounter_type)
        visits.set_visit_date_today()
        visits.submit_visit()
        logged_in_page.wait_for_url("**/patient-management/visit**", timeout=15000)
        assert "visit" in logged_in_page.url.lower()

    def test_visit_date_is_today(self, logged_in_page, base_url):
        visits = VisitsPage(logged_in_page)
        visits.navigate()
        visits.click_add_button()
        visits.set_visit_date_today()
        today = datetime.now().strftime("%m/%d/%Y")
        date_val = visits.get_visit_date_value()
        assert today in date_val

    def test_encounter_type_random_selection(self, logged_in_page, base_url):
        visits = VisitsPage(logged_in_page)
        visits.navigate()
        visits.click_add_button()
        encounter_type = random.choice(TestData.ENCOUNTER_TYPES)
        visits.select_encounter_type(encounter_type)
        selected = visits.get_selected_encounter_type()
        assert encounter_type in selected


@pytest.mark.negative
class TestVisitsNegative:
    def test_add_visit_without_patient(self, logged_in_page, base_url):
        visits = VisitsPage(logged_in_page)
        visits.navigate()
        visits.click_add_button()
        visits.submit_visit()
        logged_in_page.wait_for_timeout(2000)
        assert "new" in logged_in_page.url or visits.has_validation_error()

    def test_add_visit_without_physician(self, logged_in_page, base_url):
        visits = VisitsPage(logged_in_page)
        visits.navigate()
        visits.click_add_button()
        visits.select_patient(TestData.PATIENT_NAME)
        visits.submit_visit()
        logged_in_page.wait_for_timeout(2000)
        assert "new" in logged_in_page.url or visits.has_validation_error()


@pytest.mark.ui
class TestVisitsUI:
    def test_visits_table_columns(self, logged_in_page, base_url):
        visits = VisitsPage(logged_in_page)
        visits.navigate()
        assert visits.has_table_headers()

    def test_encounter_types_available(self, logged_in_page, base_url):
        visits = VisitsPage(logged_in_page)
        visits.navigate()
        visits.click_add_button()
        types = visits.get_encounter_types()
        assert len(types) > 0
        for et in TestData.ENCOUNTER_TYPES:
            assert et in types
