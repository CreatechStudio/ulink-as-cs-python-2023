import re
import random
import string

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

def generate_password(length=12):
    while True:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        if is_valid_password(password, username):
            return password

username = input("Enter a username: ")

print("1. Enter a password")
print("2. Generate a password")

choice = input("Choose an option: ")

if choice == "1":
    password = input("Enter a password: ")
    if is_valid_password(password, username):
        print("Password is valid.")
    else:
        print("Password is not valid.")
elif choice == "2":
    password = generate_password()
    print("Generated password:", password)
else:
    print("Invalid choice.")
