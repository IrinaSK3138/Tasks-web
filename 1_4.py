# Задание 1:
from sys import argv

def fun():
    print(argv)
    path, a, b, c = argv
    a, b, c = map(int, argv[1:])
    print('a=', a, 'b=', b, 'c=', c)
    result = a * b + c
    return result

print(fun())


# Задание 2: Целых три варианта решения получились)
list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

spisok = [list[i] for i in range(1, len(list), 1)  if list[i - 1] < list[i]]
print(spisok)

# spisok = []
# for i in range(1, len(list), 1):
#     print(i)
#     if list[i - 1] < list[i]:
#         spisok.append(list[i])
# print(spisok)

# new = [j for i, j in zip(list, list[1:]) if j > i]
# print(new)

# Задание 3:
listik = [num for num in range(20, 241) if num % 20 == 0 or num % 21 == 0]
print(listik)

# Задание 4:
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = [ll for ll in my_list if my_list.count(ll) == 1]
print(new_list)

# new_list = []
# for ll in range(len(my_list)):
#     m = 0
#     for cc in range(0, len(my_list)):
#         if my_list[ll] == my_list[cc]:
#             m = m + 1
#     if m == 1:
#         new_list.append(my_list[ll])
# print(new_list)

# Задание 5:
from functools import reduce
li = [li for li in range(100, 1001, 2)]
print(li)

def proiz(p, o):
    return p * o

print(reduce(proiz, li))

# Задание 6:
# from itertools import count
from itertools import cycle
#
# for w in count(3):
#     if w > 15:
#         break
#     print(w)

def func_6():
    c = 0
    while True:
        list_6_1 = input('Введите элементы. Для выхода нажать . ').split()
        kolvo = int(input('Сколько раз будем печатать? '))
        for elem in cycle(list_6_1):
            c += 1
            if c > kolvo:
                return
            print(list_6_1)
        break
func_6()

# Задание 7: Вариант 1
# def fact():
#     f = 1
#     num = int(input('Введите число: '))
#     for i in range(1, num + 1):
#         f = f * i
#         print(f'{i}! = {f}')
# fact()

# Задание 7: Вариант 2
from functools import reduce
num1 = int(input('Введите число: '))
def fact2():
    f = 1
    for n in (f * i for i in range(1, num1 + 1)):
        yield n

def itog(f, g):
    e = f * g
    print(f'{g}! = {e}')
    return e

massiv = []
for el in fact2():
    massiv.append(el)
print(massiv)


if num1 == 0:
    print(f'0! = 1')
else:
    print(f'1! = 1')
    print('Итог:', reduce(itog, massiv))


