
from re import fullmatch

variable_name=input("enter the variable name> \n")

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matches=fullmatch(pattern,variable_name)

print("invalid"if matches==None else "valid")