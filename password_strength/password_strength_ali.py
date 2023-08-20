'''
q:
你能否书写一段程序，来判断一个密码是否符合以下条件：
1. 至少8位
2. 至少一个大写字母，一个小写字母，一个数字，一个特殊字符
3. 不能包含个人信息（个人信息可以事先通过 input 获取）
'''

import re

def is_valid_password(password, personal_info):
    # 至少8位
    if len(password) < 8:
        return False

    # 至少一个大写字母，一个小写字母，一个数字，一个特殊字符
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif re.search("[@!#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", char):
            has_special = True

    if not has_upper or not has_lower or not has_digit or not has_special:
        return False

    # 不能包含个人信息
    if any(char in personal_info for char in password):
        return False

    return True

# 判断一个密码是否符合条件
password = input("请输入密码：")
personal_info = input("请输入个人信息：")
if is_valid_password(password, personal_info):
    print("密码符合条件")
else:
    print("密码不符合条件")
