

f_read=open("//Users//shameershajahan//Desktop/PythonJune//fileoperator//write_year.txt","r")
f_century=open("/Users/shameershajahan/Desktop/PythonJune/fileoperator/century.txt","w")
f_non_century=open("/Users/shameershajahan/Desktop/PythonJune/fileoperator/non_century.txt","w")

for year in f_read:

    y=int(year.rstrip("\n"))

    if (y%100==0):

        f_century.write(str(y)+("\n"))

    else:

        f_non_century.write(str(y)+("\n"))


