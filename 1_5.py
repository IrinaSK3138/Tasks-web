# Задание 1
    f = open('test.txt', 'w', encoding='utf-8')                             # открытие файла
while True:
    str = input('Введите строку. Пустая строка - окончание ввода')          # получение строки
    print(str)
    if str == '':                                                           # если строка пуста - стоп
        break
    f.write(str + '\n')                                                     # записать в файл
f.close()

Задание 2
file = open('Ex2.txt', 'r', encoding='utf-8')
text = file.read()
print('Количество строк:', text.count('\n') + 1)                   # +1 потому что в последней строке нет \n

file.seek(0)                                                       # в начало файла

list = file.readlines()
print(list)
for line in list:
    word = len(line.split())
    print(f'Слов в строке: {word}')
file.close()

# Задание 3
file3 = open('Ex3.txt', 'r', encoding='utf-8')
text3 = file3.readlines()
dict = {}
for z in text3:                                     # положила данные в словарь. Фамилия: сумма
    key, value = z.split()
    dict[key] = value
print(dict)
p = 0
summa = 0
for k, v in dict.items():
    v = int(v)
    if v <= 20000:
        p += 1
        summa += v
print(summa / p)
file3.close()

# Задание 4
file4 = open('Ex4.txt', 'r+', encoding='utf-8') # Открыла файл на чтение и запись
text4 = file4.readlines()                       # Взяла из него список строк
print(text4)
itog = []
eng = ['One', 'Two', 'Three', 'Four']           # Создала два списка со значениями
rus = ['Один', 'Два', 'Три', 'Четыре']
for c in text4:
    num = c.split()                             # Разделила большой список на маленькие
    for i in range(len(num)):
        if num[i] in eng:                     # Ищу элементы из списка eng и заменяю их на эл-ты списка rus
            n = eng.index(num[i])
            num[i] = rus[n]
    convertList = ' '.join(map(str, num))       # Объединяю каждый маленький список в строку
    file4.seek(0)
    itog.append(convertList + '\n')             # Добавляю строки в спискок + отступ

file4.writelines(itog)                          # Добавляю строки из списка в файл
file4.close()                                   # Закрываю файл

# Задание 5
with open('Ex5.txt', 'w+', encoding='utf-8') as file5:
    print('5 4 3 5 6 7', file = file5)
    file5.seek(0)
    text5 = file5.read()
    print(text5)
    list = []
    numbers = text5.split()
    summ = 0
    for z in numbers:
        nums = int(z)
        summ = summ + nums
    print('Сумма по строке:', summ)

# Задание 6
with open('Ex6.txt', 'r', encoding='utf-8') as file6:
    text6 = file6.readlines()
    print(text6)
    dict6 = {}
    for z in text6:                                         # положила данные в словарь. Название предмета: кол-во часов
        key, *args = z.split()
        dict6[key] = args
    print(dict6)
    for key, val in dict6.items():
        stroka = val.pop(0).split('('[0]).pop(0)            # взяла первый эл-тб разделила его и взяла данные до '('
        stroka1 = val.pop(0).split('('[0]).pop(0)
        stroka2 = val.pop(0).split('('[0]).pop(0)
        if stroka == '-':                                   # проверила наличие '-', заменила на 0
            stroka = 0
        if stroka1 == '-':
            stroka1 = 0
        if stroka2 == '-':
            stroka2 = 0
        s = int(stroka) + int(stroka1) + int(stroka2)        # сложила попредметно
        dict6[key] = s
    print(dict6)

# Задание 7
import json
with open('Ex7.txt', 'r', encoding='utf-8') as file7:
    text7 = file7.readlines()
    print(text7)
    dict7 = {}
    for x in text7:                                         # создала словарь фирма: всё остальное
        key, *args = x.split()
        dict7[key] = args
    print(dict7)
    l = 0
    o_prib = 0
    for key, val in dict7.items():                           # из значений взяла последние два
        number = val.pop(1)
        number2 = val.pop(1)
        print(number)
        print(number2)
        prib = int(number) - int(number2)                   # посчитала прибыль (prib)
        print('Прибыль =', prib)

        if prib > 0:
            l += 1
            o_prib = o_prib + prib
        dict7[key] = prib                                   # в изначальный словарь положила новые значения - прибыль
    s_prib = o_prib / l                                     # посчитала среднюю прибыль s_prib (o_prib - это общая прибыль, где > 0)
    print('Средняя прибыль:', s_prib)
    print(dict7)
    d7 = {}
    d7['Средняя прибыль'] = s_prib                          # создала отдельный словарь для средней прибыли
    print(d7)
    list7 = []                                              # создала список и положила в него словари
    list7.append(dict7)
    list7.append(d7)
    print(list7)

with open('Ex7j.json', 'w', encoding='utf-8') as f:          # создала файл.json и добавила в него свой список
    json.dump(list7, f)



