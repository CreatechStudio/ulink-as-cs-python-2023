'''
write a python program that
at least one lowercase,uppercase letter,one digit, one special character, no commonn passwords, no username contain
'''

import re

COMMON_PASSWORDS = ["password123", "12345678", "qwerty"]
COMMON_USERNAMES = ["admin", "user", "guest"]

def is_valid_password(password, username):
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    if username.lower() in password.lower():
        return False
    if password in COMMON_PASSWORDS:
        return False
    if username.lower() in COMMON_USERNAMES:
        return False

    return True

username = input("Enter a username: ")
password = input("Enter a password: ")

if is_valid_password(password, username):
    print("Password is valid.")
else:
    print("Password is not valid.")
