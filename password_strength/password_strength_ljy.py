# Aug 18
import re
import string
import random

COMMON_WORDS = ["password123", "12345678", "qwerty", "password"]
VALID_CHARS = list(string.ascii_letters + string.digits + string.punctuation)


def check(password: str, name: str):
    COMMON_WORDS.append(name)
    preq = re.search(
        "(?=.*[a-z].*)(?=.*[A-Z].*)(?=.*\d.*)(?=.*[$@$!%*?&].*)[A-Za-z\d$@$!%*?&]",
        password,
    )
    common = True
    for w in COMMON_WORDS:
        common = common and not (w in password)
    namein = name in password.lower()
    return preq and common and len(password) >= 8


if __name__ == "__main__":
    name = input("What is your name: ").strip().lower()
    while True:
        mode = input(
            "Choose the service:\n1 Check a password\t2 Generate a password\t3 Quit\n"
        ).strip()

        if mode == "1":
            if check(password=input("The password: "), name=name):
                print("It passes.")
            else:
                print("It fails")

        elif mode == "2":
            l = int(input("How long: "))
            while True:
                p = "".join(random.choices(VALID_CHARS, k=l))
                if check(p, name):
                    print(p)
                    break

        else:
            break
