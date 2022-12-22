# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8

from random import randint

number = int(input('Введите размер списка: '))
list = []
summ = 0
for i in range(number):
    list.append(randint(1, 10))
    if i % 2 == 0:
        summ = summ + list[i]


print(list)
print(f'Сумма нечетных позиций чисел равна {summ}')



# number = int(input('Введите размер списка '))
# list = []
# sum = 0
# for i in range(number):
#     list_number = int(input(f'Введите число {i+1} '))
#     list.append(list_number)
#     if i % 2 == 0:
#         sum += list[i]


# print(list)
# print(f'Сумма нечетных чисел равна {sum}')
