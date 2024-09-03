
from re import fullmatch

f=open("/Users/shameershajahan/Desktop/PythonJune/regularExpression/domain.txt")

for line in f:

    domain=line.rstrip("\n")

    pattern="[\w\W]+\.com"

    matcher=fullmatch(pattern,domain)

    if matcher!=None:

        print(domain)