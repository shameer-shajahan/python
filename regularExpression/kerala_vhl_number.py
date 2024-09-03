
# kerala vehicle number valid or not



from re import fullmatch

number=input("enter the number>\n")

pattern="(KL)\s?[0-9]?[1-9]\s?[A-Z][A-Z]?\s?[0-9]{4}"

matchs=fullmatch(pattern,number)

print("invalid" if matchs==None else "valid")

