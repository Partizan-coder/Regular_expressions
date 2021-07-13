# -*- coding: utf-8 -*-

from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
f.close()
# TODO 1: выполните пункты 1-3 ДЗ

for i in range(len(contacts_list) - 1):
    fio_row = contacts_list[i+1][0].split(sep=" ")
    if len(fio_row) == 3:
        contacts_list[i+1][0] = fio_row[0]
        contacts_list[i+1][1] = fio_row[1]
        contacts_list[i + 1][2] = fio_row[2]
    elif len(fio_row) == 2:
        contacts_list[i + 1][0] = fio_row[0]
        contacts_list[i + 1][1] = fio_row[1]
    fio_row = contacts_list[i+1][1].split(sep=" ")
    if len(fio_row) != 1:
        contacts_list[i+1][1] = fio_row[0]
        contacts_list[i+1][2] = fio_row[1]

condition = True
while condition:
    removing_element = 0
    count = len(contacts_list)
    for i in range(count - 2):
        for j in range(count -(i+2)):
            if contacts_list[i+1][0] == contacts_list[i+2+j][0]:
                if contacts_list[i+1][1] == contacts_list[i+2+j][1]:
                    for k in range(5):
                        if len(contacts_list[i+1][k+2]) < len(contacts_list[i+2+j][k+2]):
                            contacts_list[i + 1][k + 2] = contacts_list[i+2+j][k+2]
                    removing_element = i+2+j
    if removing_element == 0:
        condition = False
    contacts_list.remove(contacts_list[removing_element])

# pattern_number_1 = '(\+7|8)?\s*\((\d+)\)\s*(\d+)[\s-]*(\d+)[\s-](\d+)'
# pattern_number_2 = '(\+7|8)\s(\d+)[\s-](\d+)[\s-](\d{2})(\d{2})'
# pattern_number_3 = '(\+7|8)(\d{3})(\d{3})(\d{2})(\d{2})'
# pattern_number_4 = '(\+7|8)\D(\d{3})\D(\d+)[\s-](\d+)[\s-](\d+)'
pattern_list = []
pattern_list.append('(\+7|8)?\s*\((\d+)\)\s*(\d+)[\s-]*(\d+)[\s-](\d+)')
pattern_list.append('(\+7|8)\s(\d+)[\s-](\d+)[\s-](\d{2})(\d{2})')
pattern_list.append('(\+7|8)(\d{3})(\d{3})(\d{2})(\d{2})')
pattern_list.append('(\+7|8)\D(\d{3})\D(\d+)[\s-](\d+)[\s-](\d+)')

pattern_add_1 = '[\(][д][о][б]\.\s\d+[\)]'
pattern_add_2 = '[д][о][б]\.\s\d+'

substitution_number = r'+7(\2)\3-\4-\5'
for j in range(len(pattern_list) - 1):
    print(pattern_list[j])
    for i in range(len(contacts_list)):
        contacts_list[i][5] = re.sub(pattern_list[j], substitution_number, contacts_list[i][5])

pprint(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook_result.csv", "w", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)


