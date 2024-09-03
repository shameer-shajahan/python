


mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]


# print all mobile name
# print all mobile brands

mobile_name=[mob.get("title") for mob in mobiles]
# print(mobile_name)

mobile_brand={mob.get("brand") for mob in mobiles} #// { } set
# print(mobile_brand)
# print(type(mobile_brand))


mobile_title=[mob.get("title") for mob in mobiles if mob.get("brand")=="samsung"]
# print(mobile_title)


# print all mobile price range in 23k to 40k
filter_mobile=[mob.get("title") for mob in mobiles if mob.get("price") in range(23000,40000)]
# print(filter_mobile)

# // costly mobile
cost_mob=[mob.get("price") for mob in mobiles ]
max_cost=max(cost_mob)
top_mobile=[mob.get("title") for mob in mobiles if mob.get("price")==max_cost]
print(top_mobile)

