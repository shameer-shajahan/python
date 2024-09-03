

dictionary={}
# print(type(dictionary))

# to assign a value from dictionary

# dictionary={key:value}

# // key should be unique if add a same key to print last key


dict={"name":"shameer"} # // collection elements as a key:value pair
# print(dict)


# // print(dictionary_name[key])
print(dict["name"])

dict["name"]="aseed" # // to update name 
# print(dict)

dict["course"]="fullstack" # // overwrite the value if the key is present else to add as a new pair
# print(dict)

        # IMPORTANT METHOD

new=dict.items() 
# print(new)           # // dict_items([('name', 'aseed'), ('course', 'fullstack')])
# // item are print keys and values in tuple then all dictionary value print in list then the list print tuple


# get method
# print(dictionary_name. key)


for i in dict:
    print(i)


# for i in dict:
#     print(dict[i])

# for i in dict:
#     print(f"{i} = {dict[i]}")

# for i in dict:
#     if(i=="course"):
#         dict[i]="data secience"
        
# print(dict)


# pop() to remove the key : value from the dictionary if its present

# for i in dict:
#     if i=="":


# mothod