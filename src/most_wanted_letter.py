# You are given a text, which contains different english letters
# and punctuation symbols.
# You should find the most frequent letter in the text.
# The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter,
# so for the purpose of your search, "A" == "a".
# Make sure you do not count punctuation symbols,
# digits and whitespaces, only letters.
# If you have two or more letters with the same frequency,
# then return the letter which comes first in the latin alphabet.


def checkio(text: str) -> str:
    punctuations = '''!()-[]{};:'",0123456789 <>./?@#$%^&*_~'''
    for chr in text:
        if chr in punctuations:
            text = text.replace(chr, '')
    text = text.replace('', ' ')
    text = text.casefold()
    text_list = text.split()
    text_dict = {}
    for el in text_list:
        text_dict[el] = text_dict.get(el, 0) + 1
    s = sorted(text_dict.keys(), key=text_dict.get)
    print(s)
    catch = sorted(text_dict.values())
    catch_two = sorted(text_dict.keys())
    for i in range(0, len(catch)):
        if catch[0] == catch[i] and catch[-1] == catch[0]:
            x = catch_two[0]
            return x
            break
        else:
            return s[-1]


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and
    # not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
