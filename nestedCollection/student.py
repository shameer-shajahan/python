student=[
    {"id":100,"name":"vipin","course":"django","mark":120},

    {"id":101,"name":"dipin","course":"django","mark":130},

    {"id":102,"name":"sipin","course":"testing","mark":140},

    {"id":103,"name":"fipin","course":"mernstack","mark":190},

    {"id":104,"name":"nipin","course":"django","mark":160},

    {"id":105,"name":"lipin","course":"fullstack","mark":170},

    {"id":106,"name":"ripin","course":"django","mark":140},

]

# // print all student names

names=[dic.get("name") for dic in student]
# print (names)


# // print all  student course
course=[dic.get("course") for dic in student]
# print(set(course))



# // course = djando
selected_cource=[std.get("name") for std in student if std.get("course")=="django"]
# print(selected_cource)


# // student mark above 140 and 170

st_mark=[st.get("name") for st in student if st.get("mark") in range(140,170)]
# print(st_mark)

max_mark=[st.get("mark") for st in student ]
a=max(max_mark)
name=[st.get("name") for st in student if st.get("mark")==a]
print(name)






