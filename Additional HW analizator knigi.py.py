import operator
import re
from operator import itemgetter

a = open("text2.txt", "r")  # Загоняем файл в переменную
b = a.read()

bad_chars = ['.', ',', '?']  # Формируем список лишних символов

formatted_str = ''.join(i for i in b if not i in bad_chars).replace("\n",
                                                                    " ").lower().split()  # Избавляемся от лищних символов

spisok = dict.fromkeys(set(formatted_str), )  # Создаем Словарь

for i in spisok:  # Считаем количество слов в списке
    ii = formatted_str.count(i)
    spisok[i] = ii

sort_dict = dict(sorted(spisok.items(), key=operator.itemgetter(1),
                        reverse=True))  # Сортируем словарь по значениям в обратном порядке

print(sort_dict)  # Кайфуем от самих себя созерцая результат
