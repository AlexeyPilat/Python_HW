# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

a = int(input('Введите номер четверти в которой бы хотели узнать диапозон возможных координат: '))

if a == 1:
    print('В первой четверти - x > 0 y > 0')
elif a == 2:
    print('Во второй четверти - x < 0 y > 0')
elif a == 3:
    print('В третьей четверти - x < 0 y < 0')
elif a == 4:
    print('В четвертой четверти - x > 0 y < 0')
else:
    print('Такой четверти нет :(')