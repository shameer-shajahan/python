num=int(input("enter the number = "))
isprime=True
for i in range (2,num):
    if(i%num==0):
        isprime=False
        break
print(f"{num} is prime" if isprime==True else f"not prime")