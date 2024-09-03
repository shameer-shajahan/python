# write a program to find bmi ?
# // bmi=(weight_in_kg/height_in_metersqure)

weight=int(input("enter the weight in kg\n"))

height=int(input("enter the height in cm\n"))

height=(height/100)

print(f"weight = {weight} kg")

print(f"height= {height} cm")

bmi=weight/height**2

print(f"your bmi = {bmi}")