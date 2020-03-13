# Dict comprehensions
# Создайте словарь с помощью генератора словарей,
# так чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел.
gag = {x: y for x in range(1, 21) for y in range(x ** 3 + 1)}
print(gag)
