import os
from datetime import datetime


class TestData:
    # CareConnect URLs
    BASE_URL = os.getenv("CC_BASE_URL", "https://qc.care-connect.health")
    LOGIN_URL = BASE_URL + "/login"
    DASHBOARD_URL = BASE_URL + "/dashboard"
    VISITS_URL = BASE_URL + "/patient-management/visit"
    NEW_VISIT_URL = BASE_URL + "/patient-management/visit/new"

    # Credentials
    USERNAME = os.getenv("CC_USERNAME", "careconnect@neorx.co")
    PASSWORD = os.getenv("CC_PASSWORD", "")

    # Facility
    FACILITY_NAME = "Naseem Al Awsat Specilized Clinic"

    # Patient
    PATIENT_NAME = "Samer al asmari samer"

    # Physician
    PHYSICIAN_NAME = "NATHEER ALI ALSHAMIMI"

    # Encounter Types available in the system
    ENCOUNTER_TYPES = ["Emergency", "Outpatient", "Virtual"]

    # Visit date - always generated dynamically at runtime
    @staticmethod
    def get_today_date():
        return datetime.now().strftime("%m/%d/%Y")

    @staticmethod
    def get_today_datetime():
        return datetime.now().strftime("%m/%d/%Y %I:%M %p")
