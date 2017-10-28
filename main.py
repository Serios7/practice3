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

path_input = input('Путь к входному файлу: ')
path_output = input('Путь к выходному файлу: ')

def read_file(path):
    try:
        with open(path) as input_file:
            text = input_file.read()
            return text
    except IOError:
        return



def count_letters(text):
    # Поиск осуществляется по регулярному выражению.
    # В качестве шаблона выступают латинские буквы.
    # С вхождением одного латиского символа.
    result = re.findall(r"[a-zA-Z]", text)
    return '%d letters' % len(result)

def count_words(text):
    result = re.findall(r"\w+", text)
    return '%d words' % len(result)

def count_lines(text):
    a = text.splitlines()
    return '%d lines' % len(a)

def print_in_file(path):
    text = read_file(path_input)
    if text is not None:
        with open(path, 'w') as output_file:
            items = [count_letters(text), count_words(text), count_lines(text)]
            for item in items:
                output_file.write("%s\n" % item)
    else:
        print("Could not read file")

print_in_file(path_output)
