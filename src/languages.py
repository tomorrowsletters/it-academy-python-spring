# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.
import random

numbers_pupils = int(input('Input number of pupils: '))
data_base = {}
pack_l = set()
count = 0
click = 0
while numbers_pupils != count:
    count += 1
    number_languages = int(input('Number of Languages: '))
    languages = input('Input Languages: ')
    list_languages = languages.split()
    data_base[languages] = number_languages
    for i in list_languages:
        pack_l.add(i)
print('Number of Languages of pupils: ', len(pack_l))
print(*pack_l)
output = random.choice(list(data_base.items()))
print(
    'At least one pupil knows {} languages - {}'.format(output[1], output[0]))
