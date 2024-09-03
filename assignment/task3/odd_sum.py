# program to print sum all odd number from 1 to 100 ?

start=1
end=100
temp=0
while(start<=end):
    if(start%2!=0):
        temp=temp+start
    start+=1
print(temp)
