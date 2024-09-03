# program to print all even number from enter limit ?

start=int(input("enter the start num = "))
end=int(input("enter the ending num = "))
for i in range(start,end):
    if(i%2!=0):
        print(i)