# 1. Напишите программу, которая считает общую цену.
# Вводится M рублей и N копеек цена, а также количество L товара.
# Посчитайте общую цену в рублях и копейках за L товаров.
dollars = int(input("Dollars: "))
cents = int(input("Cents: "))
count = int(input("Count: "))
summary_count = (dollars * 100 + cents) * count
cents = summary_count % 100
dollars = int((summary_count - cents) / 100)
print(dollars, "dollars", cents, "cents")
