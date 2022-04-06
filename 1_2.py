# Задание 1
list = [1, 45, 'Karl', False, 2.3, [1, 2]]

for object in list:
    print(type(object))

# Задание 2
list = []
i = 1

kolvo = int(input('Сколько элементов Вы хотите добавить в список? '))
while i <= kolvo:
    obj = input('Введите элемент списка: ')
    list.append(obj)
    i += 1
for num in range(0, kolvo - 1, 2):
    element = list[num]
    list[num] = list[num + 1]
    list[num + 1] = element

print(list)

# Задание 3
my_dict = {
    '1': 'Зима',
    '2': 'Зима',
    '3': 'Весна',
    '4': 'Весна',
    '5': 'Весна',
    '6': 'Лето',
    '7': 'Лето',
    '8': 'Лето',
    '9': 'Осень',
    '10': 'Осень',
    '11': 'Осень',
    '12': 'Зима'
}

list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

while True:
    month = input('Введите месяц: ')
    if month in list:
        print(f'Время года - {my_dict[month]}')
        break
    else:
        print('Введите целое значение от 1 до 12! ')

# Задание 3. Вариант 2
seasons = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

while True:
    month = input('Введите месяц: ')
    if month in list:
        print(f'Время года - {seasons[int(month) - 1]}')
        break
    else:
        print('Введите целое значение от 1 до 12! ')


# Задание 4
word = input('Введите строку: ')
a = 0

list = word.split()
for piece in list:
    a += 1
    if len(list[a - 1]) > 10:
        print(f'{a}) {str(list[a - 1])[:10]}')
    else:
        print(f'{a}) {list[a - 1]}')



# Задание 5
my_list = [7, 5, 3, 3, 2]
new_element = int(input('Введите число: '))


for num in range(0, len(my_list)):
    if my_list[num] < new_element:
        my_list.insert(num, new_element)
        break
    elif my_list[len(my_list) - 1] >= new_element:
        my_list.append(new_element)
        break

print(my_list)
