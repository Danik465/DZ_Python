# # 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и
# #    меньшее число. В качестве символа-разделителя используйте пробел.


# stroka = '3, 4, 5, 6'
# x = stroka.split(', ')
# for i in range(len(x)):
#     x[i] = int(x[i])
# max_list = x[0]
# min_list = x[0]
# for i in x:
#     if max_list < i:
#         max_list = i
#     if min_list > i:
#         min_list = i
# print(max_list, min_list)


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:


# A = int(input())
# B = int(input())
# C = int(input())

# D = (B**2) - (4*A*C)
# x1 = 0
# x2 = 0
# if D > 0:
#     x1 = (-B - D**0.5)/2*A
#     x2 = (-B + D**0.5)/2*A
#     print(x1, x2)
# elif D==0:
#     x1= -B/2*A
#     print(x1)
# else: print("Корней нет")
# print(D)


# # 3. Задайте два числа. Напишите программу, которая
# #    найдёт НОК (наименьшее общее кратное) этих двух чисел.


# num1 = int(input())
# num2 = int(input())
# num1_1 = num1
# num2_2 = num2
# while num1!=num2:
#     if num1> num2:
#         num1 -=num2
#         print(num1)
#     else:
#         num2 -= num1
#         print(num2)


# NOK = (num1_1*num2_2)/num2
# print(NOK)

# Задан целочисленный двумерный массив, состоящий из N строк и M столбцов.
# Требуется вычислить сумму элементов в каждой строке и в каждом столбце.
# from random import randint
# rows = int(input())
# colms = int(input())

# sum_rows = 0
# sum_rows_mas = []
# for i in range(1, rows+1):
#     for j in range(1, colms+1):
#         print(randint(1,10) , end="\t")
#         sum_rows += i

#     print()

# print(sum_rows)


pi = 0

p = (4 / 1) - (4 / 3) + (4 / 5) - (4 / 7) + (4 / 9) - (4 / 11) + (4 / 13) - (4 / 15) + (4 / 17) - (4 / 19) + (
            4 / 21) - (4 / 23)

i = 1
while i != 101:
    pi += 4 / i - 4 / (i + 2)
    i += 2

print(pi)
