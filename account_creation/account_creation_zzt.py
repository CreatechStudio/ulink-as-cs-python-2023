import tkinter as tk
from tkinter import messagebox
import re
import random
import string
import json
import hashlib
import os

COMMON_PASSWORDS = ["password", "123456", "qwerty", "letmein"]
COMMON_USERNAMES = ["admin", "user", "guest"]

# Get the current directory path
current_directory = os.path.dirname(os.path.abspath(__file__))

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

def has_sequential_pattern(password):
    for i in range(len(password) - 4):
        if password[i:i+5] in '01234567890abcdefghijklmnopqrstuvwxyz':
            return True
    return False

def has_repeated_pattern(password):
    for i in range(len(password) - 6):
        if password[i:i+7] in ['1234567', 'qwertyu', 'abcdefg', 'aabbcc', 'zzzxxx']:
            return True
    return False

def has_keyboard_pattern(password):
    keyboard_patterns = ['qwerty', 'azerty', 'zxcvbn', 'asdfgh', 'qazwsx', '1qaz', 'zaq1']
    return any(pattern in password for pattern in keyboard_patterns)

def generate_password(length=12):
    while True:
        password_chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_chars) for _ in range(length))
        if is_valid_password(password, username):
            return password

def save_password(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    data = {}
    try:
        with open('./passwords.json', 'r') as file:
            data = json.load(file)
            if username in data:
                return False  # Username already exists
    except FileNotFoundError:
        pass
    
    data[username] = hashed_password
    
    with open('./passwords.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    return True

def check_login():
    username = username_entry.get()
    password = password_entry.get()
    
    with open('./passwords.json', 'r') as file:
        data = json.load(file)
        if username in data and data[username] == hashlib.sha256(password.encode()).hexdigest():
            feedback = "Login successful."
        else:
            feedback = "Login failed."

    messagebox.showinfo("Login Result", feedback)

def show_generated_password():
    global username
    username = username_entry.get()
    generated_password = generate_password()
    messagebox.showinfo("Generated Password", f"Generated Password: {generated_password}")

def check_password():
    global username
    username = username_entry.get()
    password = password_entry.get()
    
    if is_valid_password(password, username):
        save_result = save_password(username, password)
        if save_result:
            feedback = "Password is valid and registered."
        else:
            feedback = "Username already exists. Password not registered."
    else:
        feedback = "Password is not valid."

    if has_sequential_pattern(password):
        feedback += "\nContains sequential pattern."
    if has_repeated_pattern(password):
        feedback += "\nContains repeated pattern."
    if has_keyboard_pattern(password):
        feedback += "\nContains keyboard pattern."

    messagebox.showinfo("Password Registration and Validation Result", feedback)

# Create a GUI window
root = tk.Tk()
root.title("Password Validator and Login")
root.geometry("518x380")

username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

validate_button = tk.Button(root, text="Register", command=check_password)
validate_button.pack()

generate_button = tk.Button(root, text="Generate Password", command=show_generated_password)
generate_button.pack()

login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack()

# Start the GUI event loop
root.mainloop()