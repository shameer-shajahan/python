# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater 20 than , print Not Weird 
num=int(input("enter the number = "))
if(num%2!=0):
    print("weird")
elif(num<=5):
    print("not weird")
elif(num<=20):
    print("weird")
elif(num>20):
    print("not weird")