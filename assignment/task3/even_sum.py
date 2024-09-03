# program to print sum all even number from 1 to 100 ?

start=1
end=100
temp=0
while(start<=end): #1<=100
    if(start%2==0): #2%2==0 true
        temp=temp+start #2=2+4=6
    start=start+1
print(temp)