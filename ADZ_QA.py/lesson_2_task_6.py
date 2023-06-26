# Задание 6: Дан список lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20].
#Необходимо вывести элементы, которые одновременно:
#   1. меньше 30,
#   2. делятся на 3 без остатка.
less = 30
div = 3

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
sm = 0

# Поочередно перебираем элементы списка
for a in lst:
    # Проверяем, что
    # 1) Текущий элемент меньше 30
    # 2) Остаток от деления текущего элемента на 3 равен 0
    if (a < less) and (a % div == 0):
        print(a)
    # Добавляем элемент к сумме, если условие не выполнено
    else:
        sm += a

# Выводим конечную сумму
print('Sum: ', sm)