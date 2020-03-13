# Даны два списка чисел.
# Посчитайте, сколько различных чисел входит только в один из этих списков
import random

first = [random.randrange(1, 9) for i in range(10)]
second = [random.randrange(1, 9) for i in range(10)]
first_set = set(first)
second_set = set(second)
first_set.symmetric_difference(second_set)
print('Unique elements: ', len(first_set))
