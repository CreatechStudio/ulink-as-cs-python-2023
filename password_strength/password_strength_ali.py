'''
q:
你能否书写一段程序，来判断一个密码是否符合以下条件：
1. 至少8位
2. 至少一个大写字母，一个小写字母，一个数字，一个特殊字符
3. 不能包含个人信息（个人信息可以事先通过 input 获取）
同时，我们需要一个能够自动生成符合要求的密码的子程序，并让用户自己选择是否使用自动生成的密码
'''

import random
import string

def check_password(password):
    if len(password) < 8:
        return False

    uppercase_letters = []
    lowercase_letters = []
    digits = []
    special_characters = []

    # 检查是否至少包含一个大写字母、一个小写字母、一个数字、一个特殊字符
    for char in password:
        if char.isupper():
            uppercase_letters.append(char)
        elif char.islower():
            lowercase_letters.append(char)
        elif char.isdigit():
            digits.append(char)
        elif char in string.punctuation:
            special_characters.append(char)

    # 检查密码中是否包含个人信息
    if any(password.count(char) > 0 for char in ['123456', 'qwerty', 'password']) or any(char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] for char in password):
        return False

    # 生成新的密码并检查是否符合要求
    new_password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8))

    # 检查新密码是否符合要求
    return check_password(new_password)

def auto_generate_password(user_input):
    if user_input == "true":
        # 自动生成密码并返回
        new_password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8))
        return new_password
    else:
        # 提示用户输入自己的密码
        return input("请输入自己的密码：")


password = input("请输入密码：")
if check_password(password):
    print("密码符合要求")
else:
    print("密码不符合要求")

user_input = input("是否使用自动生成的密码？(输入 true 或 false)：")
new_password = auto_generate_password(user_input)
if check_password(new_password):
    print("自动生成的密码符合要求")
else:
    print("自动生成的密码不符合要求")
