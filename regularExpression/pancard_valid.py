
#  //  validate pancadr number ?

# first 3 letter are alphabets 

# 4 th place must be [pcafht]

# 5th letter mustbe alphabet

# 4 digits 

# last 1 alphabets



from re import fullmatch

pancard=input("enter the number ")

pattern="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pancard)

print("invalid" if matcher==None else "valid")