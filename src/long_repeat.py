# you should find the length of the longest substring
# that consists of the same letter.
# For example, line "aaabbcaaaa" contains four substrings
# with the same letters "aaa", "bb","c" and "aaaa".
# The last substring is the longest one, which makes it the answer.


def long_repeat(line: str) -> int:
    if line == "":
        return False
    line.lower()
    maximum = pom = 0
    for i in range(0, len(line) - 1):
        if line[i] == line[i + 1]:
            pom += 1
            if pom > maximum:
                maximum = pom
        else:
            pom = 0
    return maximum + 1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and
    # not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
