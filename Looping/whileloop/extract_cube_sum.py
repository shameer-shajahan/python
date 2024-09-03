# read a program to print sum of  cube extract number ?

num=int(input("enetre a number = "))
cube=0
temp=0
while(num!=0):

    digit=num%10

    cube=digit**3

    temp=cube+temp

    num=num//10

print(temp)
