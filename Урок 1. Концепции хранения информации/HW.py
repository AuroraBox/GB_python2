#
#
# '''1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и
# также проверить тип и содержимое переменных.'''

b, s, d = 'разработка', 'сокет', 'декоратор'
print(type(b), type(s), type(d))

b__u, s__u, d__u = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0', \
                   b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82', \
                   b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'

print(b__u)
print(s__u)
print(d__u)

print(type(b__u), type(s__u), type(d__u))

#
# '''2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.'''

var_class = "\u0063\u006C\u0061\u0073\u0073"
print(type(var_class), len(var_class))
print(var_class)

var_function = '\u0066\u0075\u006E\u0063\u0074\u0069\u006F\u006E'
print(type(var_function), len(var_function))
print(var_function)

var_method = '\u006D\u0065\u0074\u0068\u006F\u0064'
print(type(var_method), len(var_method))
print(var_method)


# '''3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.'''

a = b'attribute'
# b = b'класс'
# c = b'функция'
d = b'type'




'''4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
байтовое и выполнить обратное преобразование (используя методы encode и decode).'''

a, b, c, d = 'разработка', 'администрирование', 'protocol', 'standard'
print(a, b, c, d)

a_u, b_u, c_u, d_u = a.encode('utf-8'), b.encode('utf-8'), c.encode('ascii'), d.encode('ascii')
print(a_u, b_u, c_u, d_u)

ad, bd, cd, dd = a_u.decode('utf-8'), b_u.decode('utf-8'), c_u.decode('ascii'), d_u.decode('ascii')
print(ad, bd, cd, dd)


'''5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на
кириллице.'''


import subprocess

# in_put = ['ping', 'yandex.ru']
in_put = ['ping', 'youtube.com']
sub_ping = subprocess.Popen(in_put, stdout=subprocess.PIPE)
for i in sub_ping.stdout:
    i = i.decode('cp866').encode('utf-8')
    print(i.decode('utf-8'))


'''6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
«сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и
вывести его содержимое.'''


import chardet

filename = "test_file.txt"
with open(filename, 'rb') as f:
    res = chardet.detect(f.read())
    print(res)

# with open(filename, 'r', encoding='utf-8') as file_utf8:
#     for i in file_utf8:
#         print(i)

with open(filename, 'rb') as file:
    for i in file:
        print('', i)






