
# 5) Write a program to check the given year is a leap year or not

year=int(input("enter the year\n"))

y="leap year" if year%100==0 and year%400==0 or year%4==0 and year%100!=0 else "not leap year"
print(y)


