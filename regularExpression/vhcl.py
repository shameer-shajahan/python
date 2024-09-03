from re import fullmatch

f=open("/Users/shameershajahan/Desktop/PythonJune/regularExpression/vhcl.txt")
valid_vhcl_no=open("/Users/shameershajahan/Desktop/PythonJune/regularExpression/valid_vhcl_no.txt","w")

for line in f:

    vhcl=line.rstrip("\n")

    pattern="(KL)\\s?[0-9]?[1-9]\\s?[A-Z][A-Z]?\\s?[0-9]{4}"

    matcher=fullmatch(pattern,vhcl)

    if matcher!=None:

        valid_vhcl_no.write(str(vhcl)+"\n")
