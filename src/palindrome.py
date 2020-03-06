# 7. Определите, является ли число палиндромом
# (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами
# (без конвертации числа в строку или что-нибудь еще)
palindrome = int(input("Input number:   "))
number = palindrome
reverse = 0
while number > 0:
    reminder = number % 10
    reverse = (reverse * 10) + reminder
    number = number // 10
if reverse == palindrome:
    print("Palindrome!!!")
else:
    print("Nope")
