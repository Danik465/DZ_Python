# with open("file.txt", "w") as data:
#     data.write("\nLine12122")
#     data.write("\nLine312")


# color = ["red","green", "blue"]
# data = open("file.txt", "w")
# # data.writelines(color) #разделителей не будет
# data.write("\nLine2")
# data.write("\nLine3")
#
# data.close()


# path = "file.txt"
# data = open(path , "r")
# for line in data:
#     print(line)
# data.close()
# exit()


# -----------------------------------------------------------------------------------------------------


a= (3, 4)
# print(a)
# print(a[-1])

for item in a :
    print(item)

dict = {}
dict = \
{
    "up": "W",
    "left": "A",
    "down": "S",
    "right": "D"
}
print(dict)
print(dict["left"])

for v in dict.values():
    print(v)


list1 = [1,2,3,4,5]
# list2= list1
#
#
# list1[0] = 212
#
#
# for e in list1:
#     print(e)
# print()
#
# for e in list2:
#     print(e)
print(list1)
print(list1.pop())
print(list1)
print(list1.insert(2,11))
print(list1)