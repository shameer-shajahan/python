# program `to print fibinacci series ?

num=int(input("enter the number = "))
prev=0
cu=1
print(f"{prev},{cu}",end=(","))
for i in range(1,num-1):
    fib=prev+cu
    print(f"{fib}",end=(","))
    prev=cu
    cu=fib
    
    
    