"""
Test data constants for CareConnect automation suite.
"""
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://qc.care-connect.health"
LOGIN_URL = f"{BASE_URL}/login"
FORGOT_PASSWORD_URL = f"{BASE_URL}/side-forgot-pwd"
VISITS_URL = f"{BASE_URL}/patient-management/visit"
NEW_VISIT_URL = f"{BASE_URL}/patient-management/visit/new"

# Credentials - load from .env file
VALID_USERNAME = os.getenv("CC_USERNAME", "careconnect@neorx.co")
VALID_PASSWORD = os.getenv("CC_PASSWORD", "")

# Negative test data
INVALID_USERNAME = "invalid_user@test.com"
INVALID_PASSWORD = "WrongP@ssw0rd!"
EMPTY_STRING = ""
SQL_INJECTION = "' OR '1'='1"
XSS_PAYLOAD = "<script>alert('xss')</script>"
LONG_STRING = "A" * 256

# UI expected text
EXPECTED_TITLE = "CareConnect"
EXPECTED_HEADING = "Log in"
EXPECTED_SUBHEADING = "Please enter your details"
FORGOT_PASSWORD_URL = f"{BASE_URL}/side-forgot-pwd"

# Visits module
FACILITY_NAME = "Naseem Al Awsat Specilized Clinic"
PATIENT_NAME = "Samer al asmari samer"
PHYSICIAN_NAME = "NATHEER ALI ALSHAMIMI"
ENCOUNTER_TYPES = ["Emergency", "Outpatient", "Virtual"]
