# Даны два списка чисел.
# Посчитайте, сколько различных чисел содержится одновременно
# как в первом списке, так и во втором.
import random

first = [random.randrange(1, 9) for i in range(10)]
second = [random.randrange(1, 9) for i in range(10)]
first_set = set(first)
second_set = set(second)
first_set.update(second_set)
print('Unique elements: ', len(first_set))
