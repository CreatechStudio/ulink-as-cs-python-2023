import re
import string
import random

regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&`~\[\]\=\{\}])[A-Za-z\d$@$!%*?&`~\[\]\=\{\}]{8,}'
special = list('$@$!%*?&`~[]=\{\}')

def auto_generate(name: str):
    all_chars = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + special
    r = name
    while name.lower() in r.lower() or check(r) == False:
        r = ''.join(random.sample(all_chars, 12))
    return r

def check(password):
    result = re.match(regex, password)
    try:
        if result.group() == password:
            return True
        else:
            return False
    except:
        return False

# 获取个人信息
name = input('Name: ').strip()
# 选择
def choose():
    k = int(input('\n1. Enter a Password\n2. Generate a Password\nChoose: '))

    if k == 1:
        password = input('Password: ').strip()

        # 判断无个人信息
        if name.lower() in password.lower():
            print('No Personal Information in Password')
            exit(0)

        # 正则匹配
        if check(password):
            print(f'Available Password\nHere is your password: \033[1m{password}\033[0m')
        else:
            print(f'Password Need at Lease one capital letter, one small case letter, a number and a special character. \nHere is a sample: \033[1m{auto_generate(name)}\033[0m')
            choose()

    elif k == 2:
        password = auto_generate(name)
        print(f'Here is your password: \033[1m{password}\033[0m')

    else:
        print('Unknown Choose. Try again...')
        choose()

# main
choose()
