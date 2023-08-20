import re

regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}'

# 获取个人信息
name = input('Name: ').strip()
password = input('Password: ').strip()

# 判断无个人信息
if name.lower() in password.lower():
    print('No Personal Information in Password')
    exit(0)

# 正则匹配
result = re.match(regex, password)
try:
    if result.group() == password:
        print('Available Password')
    else:
        print('Password Need at Lease one capital letter, one small case letter, a number and a special character')
except:
    print('Password Need at Lease one capital letter, one small case letter, a number and a special character')
