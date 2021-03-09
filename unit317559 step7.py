"""
URL: https://stepik.org/lesson/334150/step/7?unit=317559
is_palindrome - alphabetic only
"""

# my solution:
def is_palindrome(text):
    text_alph = ''.join(ch for ch in text.lower() if ch.isalpha())
    for i in range(len(text_alph)//2):
        if text_alph[i] != text_alph[-i-1]:
            return False
    return True

# alternative solution:
def is_palindrome(text):
    text_alph = [i.lower() for i in text if i.isalpha()]
    return text_alph == text_alph[::-1]