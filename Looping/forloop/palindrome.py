# write a progam to print palindrome or not ?

num=int(input("enter the number = "))
result=0
value=num
while(num!=0): #2
    digit=num%10 #2
    result=result*10+digit
    num=num//10
if(result==value):
    print("number is palindrome")
else:
    print("not palindrome")
