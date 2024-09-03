
mobile={"name": "iphone_13", "brand" : "apple", "price":50000,"is_available":"true","offer":500}

if "offer" in mobile:
    selling_price=mobile.get("price")-mobile.get("offer")
    print(selling_price)
else:
    selling_price=mobile.get("price")
    print(selling_price)