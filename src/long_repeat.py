def long_repeat(line: str) -> int:
    if line == "":
        return False
    line.lower()
    max = pom = 0
    for i in range(0, len(line) - 1):
        if line[i] == line[i + 1]:
            pom += 1
            if pom > max: max = pom
        else:
            pom = 0
    return (max + 1)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and
    # not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
