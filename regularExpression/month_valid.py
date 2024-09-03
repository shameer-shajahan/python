
from re import fullmatch

month=input("enter the month\n")

pattern="(0?[1-9]|1[1-2])"

matches=fullmatch(pattern,month)

print("invalid"if matches==None else "valid")