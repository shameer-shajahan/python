# program to print all even number from enter limit ?

start=int(input("enter the first number = "))
end=int(input("enter the limit number = "))
while(start<=end):
    if(start%2!=0):
        print(start)
    start+=1