from math import pi
# # 1. Напечатать таблицу умножения, сложения и возведения в степень
#
def mylt(x,y):
    return x*y
def sum(x,y):
    return  x+y
def pow(x,y):
    return  x**y

def print_operation_table(op, num_rows=9, num_colms=9):
    for i in range(1, num_rows + 1):
        for j in range(1, num_colms + 1):
            print(op(i,j), end='\t')
        print()
#
print(print_operation_table(sum,5, 5))
print()
print(print_operation_table(mylt,5, 5))


 # 2 Напишите такое lambda выражение, чтобы получить копию values


values = [1,2,3,4,5,6,7,8,9,0]
trasformation = lambda x: x
transformed_values = list(map(trasformation, values))
print(transformed_values)
if values == transformed_values:
    print('ok')
else: print('no')

# # 3 Напишите функцию, которая проверяет, все ли объекты имеют одинаковове значение некоторой характеристики

values = [11,2,4,6,8,10]

def same_by(op, values):
    arr = [x for x in values if op(x)]
    if arr == values:
        return True
    else: return False

print(same_by(lambda x: not x%2,values))
# print(same_by(lambda x: not x%2, values))

if same_by(lambda x: not x%2,values):
    print("same")
else: print("dif")

# 4 Назвать самую дальнюю планету , с наибольшей площадью

def Area(x,y):
    return pi*x*y

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(orbits):
    area=[Area(x[0],x[1]) for x in orbits if x[0] != x[1]]
    for x in orbits:
        if max(area) == Area(x[0],x[1]):
            return x
print(*find_farthest_orbit(orbits))


# 5
vowel = 'аеёиоуэюя'
words = input().split()
res = list()

for i in words:
    res.append([j for j in i if j in vowel])
res = (list(map(lambda x: len(x), res)))
for i in range(1, len(res) - 1):
    if res[0] != res[i]: flag = False

if flag == True: print('Парам пам-пам')
else: print('Пам парам')
