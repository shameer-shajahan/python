from re import finditer

text="aliejhjsna---l---ijdjhali"

matchs=finditer("---",text)

count=0

for m in matchs:

    print(m.start(),"==",m.group())

    count=+1

print(count)






