from PySide6.QtWidgets import *
import string
import random
import re
import json
import hashlib

regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&`~\[\]\=\{\}])[A-Za-z\d$@$!%*?&`~\[\]\=\{\}]{8,}'
special = list('$@$!%*?&`~[]=\{\}')

def check(password):
    result = re.match(regex, password)
    try:
        if result.group() == password:
            return True
        else:
            return False
    except:
        return False

class UserSystem:
    def __init__(self):
        self.path = 'account_creation_wzq.json'
        self.data = {}

        try:
            self.load_data()
        except:
            open(self.path, 'w').close()
            self.load_data()

        self.message = ''

    def load_data(self):
        with open(self.path, 'r') as f:
            t = f.read()
            if t:
                self.data = json.loads(t)

    def check(self, name, password):
        if name in self.data:
            if self.load_password(password) == self.data[name]:
                return True
            else:
                self.message = f'Wrong Password'
        else:
            self.message = f'There is not a user named as {name}'
            return False

    def add(self, name, password):

        if name in self.data:
            self.message = f'There is already a user named as {name}'
            return False
        else:
            self.data[name] = self.load_password(password)
            self.save()
            self.message = f'Successfully added {name}'
            return True

    def load_password(self, p):
        return hashlib.sha256(p.encode('utf-8')).hexdigest()

    def save(self):
        with open('account_creation_wzq.json', 'w') as f:
            f.write(json.dumps(self.data))


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user_system = UserSystem()

        self.setWindowTitle("Account Create")

        self.w = 500
        self.h = 300
        self.resize(self.w, self.h)
        self.setMinimumSize(self.w, self.h)
        self.setMaximumSize(self.w, self.h)

        self.username_input = QLineEdit(self)
        self.username_input.move(5, 10)
        self.username_input.resize(460, 40)
        self.username_input.setPlaceholderText('Username')
        self.password_input = QLineEdit(self)
        self.password_input.move(5, 60)
        self.password_input.resize(460, 40)
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_bt = QPushButton('Login', self)
        self.login_bt.clicked.connect(self.submit)
        self.login_bt.resize(150, 50)
        self.login_bt.move(5, 110)

        self.register_bt = QPushButton('Register', self)
        self.register_bt.clicked.connect(self.register)
        self.register_bt.resize(150, 50)
        self.register_bt.move(5, 160)

        self.generate_bt = QPushButton('Generate Password', self)
        self.generate_bt.clicked.connect(self.generate)
        self.generate_bt.resize(150, 50)
        self.generate_bt.move(5, 210)

        self.qss()

    def qss(self):
        self.sheet = """
            QPushButton {
                border: 1px solid rgb(195, 195, 195);
                border-radius: 3px;
                background-color: rgb(255, 255, 255);
                margin: 5px;
            }

            QPushButton:hover {
                background-color: rgb(226, 226, 226);
            }

            QPushButton:pressed {
                background-color: rgb(150, 150, 150);
            }

            QLineEdit {
                border: 1px solid rgb(195, 195, 195);
                border-radius: 3px;
                padding-left: 3px;
            }

            QLineEdit:focus {
                border: 1px solid black;
            }

            QTextEdit {
                border-radius: 3px;
                border: 1px solid rgb(195, 195, 195);
                margin: 5px;
                color: black;
                font-size: 15px;
            }
        """

        self.setStyleSheet(self.sheet)

    def submit(self):
        if self.user_system.check(self.username_input.text(), self.password_input.text()):
            self.alert("Login Successfully!")
        else:
            self.alert(self.user_system.message)

    def generate(self):
        name = self.username_input.text()
        all_chars = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + special

        r = ''.join(random.sample(all_chars, 12))

        while (name.lower() in r.lower() and name != '') or check(r) == False:
            r = ''.join(random.sample(all_chars, 12))

        self.password_input.setText(r)

        return r

    def register(self):
        name = self.username_input.text()
        password = self.password_input.text()

        if name == '':
            self.alert("Username Cannot be Empty!")
            return

        if password == '':
            self.alert("Password Cannot be Empty!")
            return

        if check(password) == False:
            sample = self.generate()
            self.alert(f"Password is not valid! \nA password needs at lease one capital letter, one small case letter, a number and a special character. \nHere is a sample: {sample}")
            return

        if self.user_system.add(name, password):
            self.alert("Register Successfully!\nPlease Login")
        else:
            self.alert(self.user_system.message)

    def alert(self, msg):
        alert = QMessageBox()
        alert.setText(msg)
        alert.exec()

if __name__ == "__main__":
    app = QApplication([])
    root = MainWindow()

    root.show()
    app.exec()
