# Задание 2: Создайте функцию is_year_leap, принимающую 1 аргумент — год (число) — и возвращающую True, если год високосный, и False — иначе

def is_year_leap(x):

	if x % 4 == 0:
		if x % 4 == 0:
			print('True')
		else:
			print('False')
	else:
		print('False') 
			
is_year_leap(int(input('Введите год: ')))