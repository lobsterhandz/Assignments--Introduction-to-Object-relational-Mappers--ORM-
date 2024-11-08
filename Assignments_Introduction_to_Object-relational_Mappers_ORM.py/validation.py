# validation.py: Contains validation functions for various inputs.

import re
from datetime import datetime

def validate_email(email):
    """ Validate email format using regex """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    return False

def validate_phone(phone):
    """ Validate phone number to ensure it is numeric and of reasonable length """
    if phone.isdigit() and 7 <= len(phone) <= 15:
        return True
    return False

def validate_date(date_str):
    """ Validate date format YYYY-MM-DD HH:MM:SS """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None

def validate_positive_integer(value):
    """ Ensure a value is a positive integer """
    return isinstance(value, int) and value > 0

def validate_required_fields(data, required_fields):
    """ Ensure that all required fields are present in the data dictionary """
    missing_fields = [field for field in required_fields if field not in data or not data[field]]
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    return True, None
