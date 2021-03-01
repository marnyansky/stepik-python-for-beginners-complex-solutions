#url: https://stepik.org/lesson/303083/step/13?thread=solutions&unit=284990
"""
На вход программе подается строка текста. Напишите программу, которая выводит на экран символ, который появляется наиболее часто. Текст может содержать строчные и заглавные буквы английского и русского алфавита, а также цифры.
"""

s = input()
max_cnt = 0
freq_char = 0
for i in s:
    if s.count(i) >= max_cnt:
        max_cnt = s.count(i)
        freq_char = i
print(freq_char)