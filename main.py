# Вариант №3
# 3. Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк. Выведите три найденных числа в формате, приведенном в примере.
# Пример входного файла:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Пример выходного файла:
# Input file contains:
# 108 letters
# 20 words
# 4 lines

import re

file = open('C:\\Users\\123\\Desktop\\test.txt')

def countLetters(file):
    text = file.read()
    result = re.findall(r"[a-zA-Z]+", text)
    return result

def countWords(file):
    pass

def countLines(file):
    a = file.readlines()
    return len(a)

print()

