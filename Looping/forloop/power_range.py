# print power rangec?

num=int(input("enter the number = "))
power=0
total=0
for i in range(1,num+1):
    power=power*10+num
    total=total+power
print(total)