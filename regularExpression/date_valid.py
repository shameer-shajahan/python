
from re import fullmatch

date=input("enter the date\n")

pattern="(0?[1-9]|1[0-9]|2[0-9]|3[01])"

matches=fullmatch(pattern,date)

print("invalid"if matches==None else "valid")     