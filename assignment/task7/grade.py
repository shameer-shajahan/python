
# 4) Write  a program for grade classification based on percentage

# conditions
# percentage = 90 grade A
# percentage in between 80-90 grade B
# percentage in between 70-80 grade C
# percentage less than 70 fail


percentage=int(input("enter the percentage\n"))

if percentage >=90:

    print(" A Grade ")

elif percentage >=80 and percentage<90:

    print(" B Grade ")

elif percentage >=70 and percentage<80:

    print(" C Grade ")

else:

    print(" Fail ")


