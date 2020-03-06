# 5. Посчитать количество строчных (маленьких) и прописных (больших)
# букв в введенной строке. Учитывать только английские буквы.
import re

open_up = input("Input line:    ")
Up = re.findall('([A-Z])', open_up)
Low = re.findall('([a-z])', open_up)
print("Upper letters: ", len(Up))
print("Lower letters: ", len(Low))
