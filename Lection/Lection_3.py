# def f(x):
#     return x**2
#
#
# g = f
# print(f(1))
# print(g(1))

#
# def f(x):
#     return x**2
#
#
# g = f
# print(type(f))


# def calc(x):
#     return  x+10
#
# # print(calc(10))
# def calc2(x):
#     return  x*10
#
# # print(calc2(10))
#
# def math(op, x):
#     print(op(x))
#
# math(calc2,10)
# math(calc,10)
#
# def sum(x,y):
#     return x+y
#
#
#
# def mul(x,y):
#     return x*y
#
#
# def calc(op, a,b):
#     print(op(a,b))
#     # return op(a,b)
#
# calc(lambda x,y: x+y,2,3)


# list = []
#
# for i in range(1,101):
#     if(i%2==0):
#         list.append(i)
#
# print(list)

# path = 'C:/Users/dan_c/Desktop/PyCharm/Lection/File2.txt'
#
# f = open(path, 'r')
# data = f.read() + ''
# f.close()
#
# numbers = []
#
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]
#
# out = []
#
# for e in numbers:
#     if not e%2:
#         out.append(e,e**2)
# print(numbers)
# #
# def f(x):
#     return  x**2
#
# list_1= [(i,f(i)) for i in range(1,21) if i%2 == 0]
# print(list_1)

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 4 5 7 8 23 43 66 32'.split()

res = select(int, data)
res = where(lambda x:not x%2, res)
res = select(lambda  x: (x, x**2), res)
print(res)