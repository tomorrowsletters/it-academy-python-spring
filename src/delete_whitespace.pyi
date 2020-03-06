# 4. Вводится строка.
# Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".
words = input("Input line  ")
out = []
for i in range(0, len(words)):
    counter = 0
    for j in range(0, len(words)):
        if i != j and words[i] == words[j]:
            counter += 1
        if j == (len(words) - 1) and counter == 0:
            if words[i] not in out and words[i] != ' ':
                out += words[i]
fin = ''.join(out)
print(fin)
