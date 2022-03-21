# Задание 1
name = 'Ирина'
print(name)

age = input('Сколько Вам лет? ')
print('Вы написали', int(age),'полных лет')

date = input('Какое сегодня число? ')
month = input('Какого месяца? (буквами) ')
year = input('А год? ')
print('Сегодня', date, month, year, 'года')

# Задание 2
sec = int(input('Введите количество секунд: '))
hour = 0
min1 = 0

if sec > 86400:
    print('Введенное значение больше суток!')

elif sec > 0:
    min = int(sec/60)
    sec1 = sec
    if min > 0:
        hour = int(min / 60)
        sec1 = sec - min * 60
        min1 = min - hour * 60
    #print(hour, ':', min1, ':', sec1)
    print(f"{hour}:{min1}:{sec1}")

else:
    print('Введенное число < 0. Расчет невозможен!')


# Задание 3
num = input('Введите число: ')
print(num, '+', num + num, '+', num + num + num, '=', int(num) + int(num + num) + int(num + num + num))


# Задание 4
number = int(input('Введите целое положительное число '))
max = 0


while number > 0:
    num = number % 10
    number = number // 10
    if num > max:
        max = num


if number < 0:
    print('Число меньше нуля!')
else: print(max)


# Задание 5
money = int(input('Введите сколько заработали всего: '))
anti = int(input('Введите сколько было потрачено: '))

if money > anti:
    print('Вы зарабытываете!')
    ren = int(money / anti * 100 - 100)
    print('Рентабельность:', ren, '%')
    kolvo = int(input('Введите количество сотрудников: '))
    print('Примерный доход:', int((money - anti) / kolvo), 'руб/чел')
else:
    print('Вы несёте убытки!')
    fin_pillow = int(input('Что есть в заначке? '))
    final = int(fin_pillow / (anti - money))
    print('При таких потерях у Вас', final, 'мес')



# Задание 6
a = int(input('Сколько спортсмен пробежал в первый день? '))
b = int(input('Какова цель? '))
kolvo_day = 1

if a >= b:
    print('Справился с первого раза!')


while a <= b:
    a = 1.1 * a
    kolvo_day = kolvo_day + 1
    print(f"{kolvo_day}-й день: {a:.2f}")

if a >= b:
    print('На', kolvo_day, 'день спортсмен достиг результата - не менее', b, 'км!')
