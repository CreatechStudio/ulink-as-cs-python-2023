# password strength detection

import re

with open('common_used_password.txt', 'r') as f: # read common used password from txt
    content = f.read()

def is_common(pw): # find whether the password is common used
    if content.find(pw) != -1:
        return True
    return False

def is_valid(pw): # use regular expression
    if (re.search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$@$!%*#?&])', pw) # at least one letter(upper and lower cases), number and special character
    and re.search(r'(.{8,})', pw) # at least 8 letters
    and not re.search(r'((19|20)\d\d(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01]))', pw) # not a birthday
    and not re.search(r'1(3\d|4[5-9]|5[0-35-9]|6[2567]|7[0-8]|8\d|9[0-35-9])\d{8}', pw) # not a telephone number
    and not is_common(pw) # not a common password
    ):
        return True
    return False


# password = 'asfhkjh1231*&%!@bjAFSs'
password = input('Enter Password: ')

# print(is_valid(password))
if is_valid(password):
    print('Password is valid')
else:
    print('Password is not valid')