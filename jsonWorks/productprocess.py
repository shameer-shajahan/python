from json import load

f=open("/Users/shameershajahan/Desktop/PythonJune/jsonWorks/product.json")

product=load(f)

# print(len(product))

# for p in product:
#     print(p.get("title"))



# item=[p.get("title") for p in product ]
# print(item)


# item_jewelery=[p.get("title") for p in product if p.get("category")=="jewelery"]
# print(item_jewelery)



# // product price greter than 100 ?

# item_above_100=[p.get("title") for p in product if p.get("price")>100 ]
# print(len(item_above_100))
# print(item_above_100)




# // product price in range 100 and 150 ?

# item_range_100_to_150=[p.get("id") for p in product if p.get("price")>100 and p.get("price")<150 ]
# print(len(item_range_100_to_150))
# print(item_range_100_to_150) 




# //  products with most number of rating ?

def get_rating_count(dic):

    return(dic).get("rating").get("count")

top_selling_product=max(product,key=get_rating_count)

print(top_selling_product)
