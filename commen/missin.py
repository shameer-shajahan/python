
ms=[0,1,2,4,5]

n=len(ms)

sum_a=n*(n+1)//2

cr_sum=sum(ms)

missing=sum_a-cr_sum

print(missing)