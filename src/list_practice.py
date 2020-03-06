# List practice
# Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# Используйте на предыдущий список slice чтобы получить следующий:
# ['ab', 'ad', 'bc'].
# Используйте генератор списков чтобы получить следующий
# ['1a', '2a', '3a', '4a'].
# Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# Скопируйте список и добавьте в него элемент '2a'
# так чтобы в исходном списке этого элемента не было.
letters = 'abcd'
c = [i + k for i in letters for k in letters]
print(c)
print(c[1:4] + c[5:8])
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
print(c[1:4:2] + c[6:7])
# ['ab', 'ad', 'bc']
onetwothreefour = '1234'
a = 'a'
c = [i + k for i in onetwothreefour for k in a]
print(c)
# ['1a', '2a', '3a', '4a']
c.remove('2a')
print(c)

c_copy = c.copy()
c_copy.append('2a')
print('Orig ', c)
print('Copy: ', c_copy)
