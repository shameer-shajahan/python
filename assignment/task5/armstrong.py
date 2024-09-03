def arm(num): #153
    temp=num
    count=(len(str(num)))
    total=0
    while(num!=0):
        digit=num%10 #3 #5 #1
        sum=digit**count #3^3=27 5^3=125 1^3=14
        total=total+sum #153
        num=num//10 
    return True if temp==total else False
print(arm(154))