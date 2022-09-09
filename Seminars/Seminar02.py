n = [2,5,3,2,5,1]
number = int(input())
flag = False
for i in n:
    if number == i:
        flag = True
        break
if flag == True:
    print("Число входит в список")
else: print("Число не входит в список")



n = [2,5,3,6,5,1]
number = int(input())
flag = False
count = 0
for i in n:
    if number == i:
        count+=1

if flag == True:
    print("Число входит в список")
else: print("Число не входит в список")
