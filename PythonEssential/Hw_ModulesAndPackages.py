# Завдання 1
# Перепишіть домашнє завдання попереднього уроку (сервіс для скорочення посилань) таким чином, щоб у нього була основна
# частина, яка відповідала би за логіку роботи та надавала узагальнений інтерфейс, і модуль представлення, який
# відповідав би за взаємодію з користувачем. При заміні останнього на інший, який взаємодіє з користувачем в інший спосіб
# , програма має продовжувати коректно працювати.

# Виведіть із списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: цикл


# import example
# my_list = [1, 2, 5, 8, 10, 11, 18]
# print("квадрати парних чисел цього списка є", example.list2)


# Завдання 2
# Повторіть інформацію про розглянуті на уроці стандартні модулі. Ознайомтеся також із модулями calendar, heapq,
# bisect, array, enum.
# import array
# arr1=array.array('b',(1,2,3,4,5))
# print(arr1[1])
#
#
# from heapq import *
# heap=[]
# heappush(heap,1)
# heappush(heap,5)
# heappush(heap,3)
# print (heappop (heap))
#
# import bisect
#
# list3 = [1, 3, 5, 7, 9]
# x = bisect.bisect(list3, 2)
# print(x)
# list4 = [1, 3, 5, 7, 9]
# bisect.insort(list4, 2)
# print(list4)

# from enum import Enum
# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3
# print(Color.RED)
# print(repr(Color.RED))