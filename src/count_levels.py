import re
input = input("Input line:    ")
Up = re.findall('([A-Z])', input)
Low = re.findall('([a-z])', input)
print("Upper letters: ", len(Up))
print("Lower letters: ", len(Low))
