# read a program to print extract digit from number ?
# 

num=int (input("enter a number = "))

while(num!=0):

    digit=num%10

    num=num//10
    
    print(digit)

    
