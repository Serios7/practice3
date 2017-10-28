# Вариант №3
# 3. Дан файл. Определите сколько в нем букв (латинского алфавита),
# слов, строк. Выведите три найденных числа в формате, приведенном в примере.
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

input_file = open('input_file.txt')
text = input_file.read()

output_file = open('output_file.txt', 'w')

def count_letters(text):
    # Поиск осуществляется по регулярному выражению.
    # В качестве шаблона выступают латинские буквы.
    # С вхождением одного латиского символа.
    result = re.findall(r"[a-zA-Z]", text)
    return '%d letters' % len(result)

def count_words(text):
    # Поиск осуществляется по регулярному выражению.
    # В качестве шаблона выступают латинские буквы.
    # С 1 и более вхождением шаблона слева.
    result = re.findall(r"[a-zA-Z]+", text)
    return '%d words' % len(result)

def count_lines(text):
    a = text.splitlines()
    return '%d lines' % len(a)




