# write a program to print student name and 3 marks mark1

name=str(input("enter student name\n"))
mark1=int(input("enter mark1\n"))
mark2=int(input("enter mark2\n"))
mark3=int(input("enter mark3\n"))

total_mark=(mark1+mark2+mark3)
avg=(total_mark/3)

print(f"student name :{name} mark1 ={mark1}\n mark2 ={mark2}\n mark3 ={mark3}\n total marks ={total_mark}\n average of mark ={avg}")

