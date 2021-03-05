"""
url: https://stepik.org/lesson/328948/step/7?thread=solutions&unit=312239
На вход программе подается натуральное число nn, затем nn строк, затем число kk — количество поисковых запросов, затем kk строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются ВСЕ поисковые запросы.
"""

# popular variant:
s = [input() for _ in range(int(input()))]
d = [input() for _ in range(int(input()))]
for i in s:
    for j in d:
        if j.lower() not in i.lower():
            break
    else:
        print(i)

# my variant:
queries, search_results =  [], []
count = 0
for _ in range(int(input())):
    search_results.append(input())
for _ in range(int(input())):
    queries.append(input().lower())
for res in search_results:
    for i in range(len(queries)):
        if queries[i] in res.lower():
            count += 1
        if count == len(queries):
            print(res)
    count = 0
