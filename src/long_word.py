import re
str = input("Input string")
x = str.split()
first = x[0]
for test in x:
    if len(test) > len(first):
        first = test
result = re.compile('[^a-zA-Z]')
print(result.sub('', first))
