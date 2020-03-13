# Входные данные
# Программа получает на вход количество стран N.
# Далее идет N строк, каждая строка начинается с названия страны,
# затем идут названия городов этой страны.
# В следующей строке записано число M,
# далее идут M запросов — названия каких-то M городов, перечисленных выше.
countries_count = int(input('Input Number of countries: '))
cycle = 0
result = {}
output = ''
while cycle != countries_count:
    city_line = input('Input lines: ')
    cycle += 1
    city_line = city_line.split()
    result.update({x: y for x in city_line[1:] for y in city_line[:1]})
cycle = 0
request_count = int(input('Input number of requests: '))
while cycle != request_count:
    city = input('Input city: ')
    cycle += 1
    if city in result:
        output += result.get(city) + ' '
print(output)
