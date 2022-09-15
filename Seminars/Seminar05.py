# a,b = filter(int, input().split())
# print(a+b)

# arr = [int(i) for i in input().split() ]
# print(arr)

# arr = [-10,-20,-40,-50]
#
# for i in enumerate(arr):
#     print(arr)
#
#

# # 35. N натуральных числе
# lst = []
# path = "Data.txt"
# data = open(path , "r")
# for line in data:
#      print(line.split())
#      for int(i) in line.split():
# #
# #
# # print(lst)
# # data.close()
# # exit()
#
# def search_number(arr):
#     for i in range(1, len(arr)):
#         if arr[i] -1 != arr[i -1]:
#             return  i+1
#     return 'Последовательность верна'
# with open('Data.txt','r', encoding='utf-8') as file:
#     arr = [int(i) for i in file.read().split()]
#
# print(search_number(arr))
#
# from random import randint as rd
# arr = [1, 5, 3 , 4, 3, 2,6,1]
# ind_rand = rd(0, len(arr)-1)
# randomnumb = arr[ind_rand]
#
#
# arr2 = [randomnumb]
# for i in range(ind_rand+1 , len(arr)):
#     if arr[i]> randomnumb:
#         arr2.append(arr[i])
#         randomnumb = arr[i]
# print(arr2)
#
#
# stroka = 'ПривабВет, каабв твои дела? Чем сегоабв занят?'
#
# print(' '.join(list(filter(lambda x: 'абв' not in x.lower(), stroka.split()))))
#
#


# Создайте программу для игры в ""Крестики-нолики"".

dask = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

s = ''
for i in range(9):
    if i % 2 == 0:
        print('Ходит игрок 1')
        s = '0'
    else:
        print('Ходит игрок 2')
        s = 'X'

# RLE

stroka = 'aaaaaaaaaabbbbbbbbbbbccccccccc'
# ...
stroka = '10a12b9c'


# Доп


print(' '.join([chr(i) for i in range(ord('a'), ord('z') + 1)]))

