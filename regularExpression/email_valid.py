# email id valid or not?




from re import fullmatch

email=input("enter the emailid\n")

pattern="[\w][\w._]*(@gmail.com)"
# pattern="[a-z0-9._]*(@gmail.com)"

matches=fullmatch(pattern,email)

print("invalid" if matches==None else "valid")

