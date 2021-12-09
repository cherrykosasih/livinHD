import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def email_validator(email):
    """
    citation : https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    """
    if(re.fullmatch(regex, email)):
        return True
    return False
