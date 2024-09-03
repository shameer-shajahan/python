
from re import finditer

text="abc 75rfkfhijxdz#$. xyfi"

# pattern="\d"
# pattern="\D"
# pattern="\w"
# pattern="\W"
# pattern="\s"
#    " * " optional
pattern="\S"

matchs=finditer(pattern,text)

for m in matchs:

    print(m.start(),"==",m.group())

