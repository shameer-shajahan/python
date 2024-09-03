
def prime(num):
    for i in range(2,num):
        result=False if(num%i==0) else True
        return result
    
print(prime(7))