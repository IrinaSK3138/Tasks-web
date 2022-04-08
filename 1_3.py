# Задание 1:
def my_del(a, b):
    try:
        m_d = a / b
    except ZeroDivisionError:
        return \
            print('Деление на 0 запрещено!')
    return m_d

print(my_del(float(input('Введите делимое: ')), float(input('Введите делитель: '))))

# Задание 2:
def data(city, surn, email, name, tel):
    print('Данные пользователя:',surn, name, city, email, tel)
data(surn = input('Введите фамилию: '), name = input('Введите имя: '), city = input('Введите город: '),
email = input('Введите почту: '), tel = input('Введите номер телефона: ') )

# Задание 3:
def my_func(x, y, z):
    if x > y:
        if y > z:
            res = x + y
        else:
            res = x + z
    elif x > z:
        res = x + y
    else:
        res = z + y
    return res

print(my_func(11, 2, -13))

# Задание 4. Варинат 1:
def my_func1(q, w):
    q = float(input('Введите основание (любое число): '))
    w = int(input('Введите целое отрицательное число - показатель степени: '))
    proiz = q ** w
    print(proiz)

my_func1(0, 0)

# Задание 4. Вариант 2
def my_f(e, r):
    e = float(input('Введите основание (любое число): '))
    r = int(input('Введите целое отрицательное число - показатель степени: '))
    pr = abs(r)
    prres = 1
    for num in range(1, pr + 1):
        prres = prres * e
    result = 1 / prres
    return result

print(my_f(0, 0))

# Задание 5
def func():
    list_f = []
    summa = 0
    while True:
        list = input('Введите числа через пробел. (Для того, чтобы закончить, введите !): ').split()
        for number in list:
            if number == '!':
                print('Итоговая сумма: ', summa)
                print('Выход')
                return
            else:
                number = int(number)
                list_f.append(number)
                summa = sum(list_f)
        print(list_f)
        print('Сумма:', summa)

func()

# Задание 6.
def int_func():
    mes = []
    message = input('Введите строку: ').split()
    for word in message:
        if word.istitle() == False:
            word = word.title()
            mes.append(word)
        else:
            mes.append(word)
    print(' '.join(mes))
int_func()




