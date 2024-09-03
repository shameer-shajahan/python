# variable name
# first character must be alphabet => k to m
# second letter must be number that is / by 3
# followed by any number of alphabets and number @

from re import fullmatch

variable_name=input("enter the name>\n")


pattern="[k-m][369][a-zA-Z0-9@]*"

matchs=fullmatch(pattern,variable_name)

print("ivalid" if(matchs==None) else "valid")      