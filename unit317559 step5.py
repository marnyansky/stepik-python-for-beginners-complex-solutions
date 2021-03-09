"""
URL: https://stepik.org/lesson/334150/step/5?unit=317559
простой валидатор паролей

"""

# my solution:
def is_password_good(password):
    if (len(password) >= 8
            and (any(ch.isupper() for ch in password))
            and (any(ch.islower() for ch in password))
            and (any(ch.isdigit() for ch in password))):
        return True
    return False

# alternative solution 1:
def is_password_good(password):
    upp = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, upp, low, dig])

# alternative solution 2:
import re
is_password_good = lambda s: len(s)>= 8
            and re.search(r'\d',s)!=None
            and re.search(r'[A-Z]',s)!=None
            and re.search(r'[a-z]',s)!=None