n = int(input("input n:  "))
a = 0
b = 1
c = a + b
for i in range(n - 2):
    print("before", c)
    c = a + b
    print("before2", c)
    a = b
    print("before3", a)
    b = c
    print("before4", c)
    print("out", c)
