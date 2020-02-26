lis = ['a', 'b', 'c']
tul = tuple(lis)
print(tul)
# Convert to tuple
tul = ('a', 'b', 'c')
lis = list(tul)
print(lis)
#  a = 'a', b=2, c=’python
a, b, c = 'a', 2, 'python'
print(a, b, c)
# len 1
tul = ([1, 2, 3],)
for i in tul[0]:
    print(i)
