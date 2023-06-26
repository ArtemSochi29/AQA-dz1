# Задание 5: Напишите функцию month_to_season(), которая принимает 1 аргумент — номер месяца — и возвращает название сезона, к которому относится этот месяц.
# Например, передаем 2, на выходе получаем «Зима»

def month_to_season(month):

    if month == 12 or month < 3:
        print ("Зима")
    elif month == 3 or month < 6:
        print ("Весна")
    elif month == 6 or month < 9:
        print ("Лето")
    else:
        print ("Осень")

month_to_season(int(input("Введите месяц(число):")))

