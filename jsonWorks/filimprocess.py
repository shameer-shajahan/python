

from json import load

f=open("/Users/shameershajahan/Desktop/PythonJune/packages/jsonWorks/filims.json")

filim=load(f)

for f1 in filim:

    print(f1.get("title"))


