# write a program to find bm
# bmi=(weight_in_kg/height_in_metersqure)
# weight_in_kg=72
# height_in_metersqure
# 165cm = 0.0165metersqure

weight=72
height=165
height_metre=165/100

bmi=weight/height_metre**2
print(f"{weight}/{height}={bmi}")
