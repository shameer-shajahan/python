num=int(input("enter a number = "))

orginal=num 

total=0

count_num=len(str(num))# 3

while(num!=0): # 15!=0 true

    digit=num%10 # digit=15%10 = 5

    exponent=digit**count_num # 5**3=125

    total=exponent+total # total = 125+27

    num=num//10 #num=153//10,15//10=1

print(" armstrong number" if(total==orginal) else "its not armstrog number")