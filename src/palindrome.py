palindrome = int(input("Input number:   "))
number = palindrome
reverse = 0
while (number > 0):
    reminder = number % 10
    reverse = (reverse * 10) + reminder
    number = number // 10
if reverse == palindrome:
    print("Palindrome!!!")
else:
    print("Nope")
