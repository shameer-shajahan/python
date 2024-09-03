num=int(input("enter the number = "))
prv=0
cur=1
isfib=False
if num in (0,1): # if num==0 or num==1
    isfib=True
else:
    fib=prv+cur
    while(fib<=num):
        fib=prv+cur
        prv=cur
        cur=fib
        if(fib==num):
            isfib=True
            break
print(isfib)

# def is_fibonacci(num1): #
#     previous=0
#     current=1
#     next=previous+current
#     while(next<=num1):
#         if next==num1:
#          return True
#         previous=current
#         current=next
#         next=previous+current
#     return False
# print(is_fibonacci(5))

