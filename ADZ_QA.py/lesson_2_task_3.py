# Задание 3: Напишите функцию square, принимающую 1 аргумент — сторону квадрата — и возвращающую площадь квадрата.
import math

def square(a):

	s = a * a
	return s
	
print(square(math.ceil(1.21)))