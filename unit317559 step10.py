"""
URL: https://stepik.org/lesson/334150/step/10?unit=317559
convert CamelCaseString to python_snake_string
"""

# my solution:
def convert_to_python_case(text):
    import re
    words = re.findall('[A-Z][^A-Z]*', text)
    return '_'.join([str(word.lower()) for word in words])

# alternative solution 1:
def convert_to_python_case(text):
    s = ''
    for el in text:
        if el.isupper():
            s += '_'
        s += el.lower()
    return s[1:]

# alternative solution 2:
def convert_to_python_case(text):
    s = text[0].lower()
    for c in text[1:]:
        s += ('_' + c.lower() if c.isupper() else c)
    return s