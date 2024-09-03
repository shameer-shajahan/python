# read a program to print sum  extract digit from number ?

num=int (input("enter a number = "))
temp=0
while(num!=0):

    digit=num%10
    
    temp=temp+digit

    num=num//10

print(temp)
