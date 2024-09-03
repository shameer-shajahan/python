# program to print leap year or not?

year=int(input("enter the year\n"))
if(year%100==0):
    if(year%400==0):
        print("leap year")
    else:
        print("not leap year")
elif(year%4==0):
    print("leap year")
else:
    print("not leap year")
    