from re import finditer

text="abc378hk73hhj"

# pattern="[a-z]{3}" to add the count of pattern
pattern="[c-ht-z]"

matches=finditer(pattern,text)

for p in matches:

    print(p.start(),"==",p.group())

              



    