import json
import re
import os
import string

COMMON_WORDS = ["password123", "12345678", "qwerty", "password"]
VALID_CHARS = list(string.ascii_letters + string.digits + string.punctuation)


def check(password: str, name: str):
    preq = re.search(
        "(?=.*[a-z].*)(?=.*[A-Z].*)(?=.*\d.*)(?=.*[$@$!%*?&].*)[A-Za-z\d"
        + string.punctuation
        + "]",
        password,
    )
    common = True
    for w in COMMON_WORDS:
        common = common and not (w in password)
    namein = name in password.lower()
    return preq and common and len(password) >= 8


acc_info = dict()

if __name__ == "__main__":
    # handle storage file
    if not os.path.isfile("./account_creation_ljy.json"):
        with open("./account_creation_ljy.json", "w") as f:
            f.write(r"{}")
    with open("./account_creation_ljy.json", "r") as f:
        acc_info = json.load(f)
    f = open("./account_creation_ljy.json", "w")

    # main loop
    while True:
        try:
            choice = input("The System\n1 Login\t\t2 Register\tq quit\n").lower()
            if choice == "1":
                username = input("Your username: ").strip()
                while username not in acc_info:
                    username = input("No such user!\nRetry username: ").strip()

                input_counter = 5
                pwd = input("Your password: ").strip()
                while not pwd == acc_info[username]:
                    if input_counter > 0:
                        input_counter -= 1
                    else:
                        print("Too many trials!")
                        break
                    pwd = input("Wrong!\nRetry password: ").strip()
                if input_counter != 0:
                    print("Logged in.")
                    print("Here may provide some functions...")

            elif choice == "2":
                username = input("Your username: ").strip()
                while username in acc_info:
                    username = input("Duplicate account!\n Retry: ").strip()
                pwd = input("Your password: ").strip()
                while not check(pwd, username):
                    print("Too weak password!")
                    pwd = input("Better password: ").strip()
                acc_info.update({username: pwd})
                json.dump(acc_info, f)
                print("Account created.")
            elif choice == "q":
                print("Bye bye")
                f.close()
                exit(0)
            else:
                print("I do not understand. Please retry...")
            print("\n\n")
        except KeyboardInterrupt:
            print("\nTo quit, input 'q' in the prompt.\n")
