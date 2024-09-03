# mobile number with country code

from re import fullmatch

mobile_number=input("enter the mobile_number\n")

pattern="(91)\s?[6-9]\d{9}"

matches=fullmatch(pattern,mobile_number)

print("invalid"if matches==None else "valid")