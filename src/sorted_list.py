lis = [1, 0, 3, 0, 3, 0, 6, 3, 2, 1, 0, 1]


def sorting(sord):
    return sord == 0


lis.sort(key=sorting)
print(lis)
