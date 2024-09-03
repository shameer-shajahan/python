

def fib(num):
    prv=0
    cur=1
    next=prv+cur
    for i in range(1,num):
        if(num==0 or num==1):
            return True
        else:
            while(next<=num):
                if(next==num):
                    return True
                    print(fib(8))
                    break 
                prv=cur
                cur=next
                fib=prv+cur
                return False
        

print(fib(8))


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
# print(is_fibonacci(0))
