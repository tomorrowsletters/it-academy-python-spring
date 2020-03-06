# 3. Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
import re

string_line = input("Input string")
x = string_line.split()
first = x[0]
for test in x:
    if len(test) > len(first):
        first = test
result = re.compile('[^a-zA-Z]')
print(result.sub('', first))
