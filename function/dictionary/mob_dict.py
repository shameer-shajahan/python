
# create the dictionary 

mobile={"name": "iphone_13", "brand" : "apple", "price":50000,"is_available":"true"}
# print(mobile)



# print(mobile.get("name"))



# all_key=mobile.keys()
# print(all_key)



# all_vales=mobile.values()
# print(all_vales)


# for v,k in mobile.items():
#     print(v,k)



# mobile.pop("is_available")
# print(mobile.get("is_available"))



mobile["offer"]="10%"
for v,k in mobile.items():
    print(v,k)