# It should be eight characters long.
# The first character should be an uppercase alphabet.
# The next two characters should be a number, but the first character should be any number from 1-9 and the second character should be any number from 0-9.
# It should be zero or one white space character.
# The next four characters should be any number from 0-9.
# The last character should be any number from 1-9.

# S71 19937



from re import fullmatch

passport=input("enter the passport number\n")

pattern="[A-Z][1-9][\d][0\s][\d]{4}[1-9]{1}"

matches=fullmatch(pattern,passport)

print("invalid" if matches==None else "valid")