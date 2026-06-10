import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.smoke
class TestDashboardSmoke:
    def test_dashboard_loads_after_login(self, logged_in_page):
        assert "dashboard" in logged_in_page.url

    def test_dashboard_page_title(self, logged_in_page):
        dashboard = DashboardPage(logged_in_page)
        title = logged_in_page.title()
        assert len(title) > 0

    def test_sidebar_visible(self, logged_in_page):
        dashboard = DashboardPage(logged_in_page)
        assert dashboard.is_sidebar_visible()

    def test_visits_nav_visible(self, logged_in_page):
        dashboard = DashboardPage(logged_in_page)
        assert dashboard.is_visits_nav_visible()

    def test_patients_nav_visible(self, logged_in_page):
        dashboard = DashboardPage(logged_in_page)
        assert dashboard.is_patients_nav_visible()


@pytest.mark.regression
class TestDashboardNavigation:
    def test_navigate_to_visits(self, logged_in_page, base_url):
        dashboard = DashboardPage(logged_in_page)
        dashboard.click_visits_nav()
        logged_in_page.wait_for_timeout(3000)
        assert "visit" in logged_in_page.url.lower()

    def test_navigate_back_to_dashboard(self, logged_in_page, base_url):
        logged_in_page.goto(base_url + "/dashboard")
        logged_in_page.wait_for_load_state("networkidle")
        assert "dashboard" in logged_in_page.url

    def test_user_info_visible(self, logged_in_page):
        dashboard = DashboardPage(logged_in_page)
        assert dashboard.is_user_info_visible()


@pytest.mark.ui
class TestDashboardUI:
    def test_facility_name_displayed(self, logged_in_page):
        dashboard = DashboardPage(logged_in_page)
        facility = dashboard.get_facility_name()
        assert facility is not None and len(facility) > 0

    def test_stats_cards_visible(self, logged_in_page):
        dashboard = DashboardPage(logged_in_page)
        assert dashboard.has_stats_cards()

    def test_quick_actions_visible(self, logged_in_page):
        dashboard = DashboardPage(logged_in_page)
        assert dashboard.has_quick_actions()
