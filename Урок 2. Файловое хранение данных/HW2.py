'''1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла); '''

import os
import csv

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []

files = [file for file in os.listdir('.') if file.endswith('.txt') and file.startswith('info')]
print(files)

for file in files:
    with open(file, 'r', newline='', encoding='cp1251') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('Изготовитель системы'):
                os_prod_list.append(line)
                print(os_prod_list, '\n')
            elif line.startswith('Название ОС'):
                os_name_list.append(line)
                print(os_name_list, '\n')
            elif line.startswith('Код продукта'):
                os_code_list.append(line)
                print(os_code_list, '\n')
            elif line.startswith('Тип системы'):
                os_type_list.append(line)
                print(os_type_list, '\n')

# def get_data():


'''
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv(). 

### 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра. 

### 3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.'''

# import os
# import chardet
# import csv
#
#
# files = [listdir for listdir in os.listdir('.') if listdir.endswith('.txt')]
# fcsv = []
#
#
# def get_data():
#     d = ['Изготовитель системы',
#          'Название ОС',
#          'Код продукта',
#          'Тип системы']
#
#     for file in files:
#         with open(file, 'r', encoding='cp1251') as f:
#             lines = f.readlines()
#             for line in lines:
#                 if any([line for _ in d if line.startswith(_)]):
#                     fcsv.append(line)
#
#             print(fcsv)
#
#
#
#
#     # for file in files_dir:
#     #     with open(file, 'r', encoding='utf-8') as f:
#     #         lines = f.readlines()
#     #         for line in lines:
#     #             if any(line for i in d if line.startswith(i)):
#     #                 print(line)
#     #                 res.append(line)
#     #
#     #             with open('отчет.csv', 'w', newline="") as ff:
#     #                 writer = csv.writer(ff)
#     #                 for row in res:
#     #                     writer.writerow(res)
#
#
# get_data()


