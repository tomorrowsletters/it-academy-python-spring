dollars = int(input("Dollars"))
cents = int(input("Cents"))
count = int(input("Count"))

while cents < 50:
    c = int((cents * count) % 100)
    index = c / 10
    d = int((dollars * count) + index)
    print(d, "dollars", c, "cents")
    break
else:
    while cents > 50:
        summaryconvert = (dollars * 100) + cents
        c = summaryconvert * count
        rest = int(c % 100)
        module = int(c // 100)
        print(module, "dollars", rest, "cents")
        break
