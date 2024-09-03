def pal(num): #121
    temp=num
    total=0
    sum=0
    while(num!=0):
        digit=num%10  #1 #2
        sum=sum*10+digit #0+1+12
        num=num//10 #12
    return True if sum==temp else False
 
print(pal(126))