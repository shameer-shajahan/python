# read a number from user 
# print fizz if num is / by 3
# print buzz if num is / by 5
# print fizzbuzz if num is / by 15

# num=int(input("enter the value\n"))
# if(num/15==0):
#     print("fizzbuzz")
# elif(num%3==0):
#     print("fizz")
# elif(num%5==0):
#     print("buzz")
# else:
#     print("no output are given")

# //logic 2

num=int(input("enter the number\n"))

result=""

if(num%3==0):

    result=result+"fix"

if(num%5==0):

    result=result+"buzz"

print(result)
