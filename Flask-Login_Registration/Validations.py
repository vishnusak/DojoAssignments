import re
EMAIL = re.compile('[a-zA-Z0-9\._-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]')

DIGIT = re.compile('[0-9]')
CAPS  = re.compile('[A-Z]')

def e_validate(email):

    is_email = EMAIL.match(email)

    if is_email:
        return True
    else:
        return False

def n_validate(name):

    if (len(name) < 2):
        return 'is_short'

    has_number = DIGIT.search(name)

    if has_number:
        return False
    else:
        return True

def p_validate(pwd):

    if (len(pwd) < 8):
        return 'is_short'

    has_number = DIGIT.search(pwd)
    has_caps = CAPS.search(pwd)

    if has_number and has_caps:
        return True
    else:
        return False
