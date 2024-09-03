#q1  print all the country in the list
#q2  total number of country
#q3  country with same languages
#q4  highest populated country
#q5  largest country
#q6  smallest country
#q7  currency of Vietnam
#q8  non independent countries
#q9  populations below 200000
#q10 Uzbekistan is independent or not
#q11 countries and their callingcodes
#q12 numeric code of United States
#q13 native name of Hungary
#q14 country have most timezone
#q15 capital of Russian Federation
#q16 print all names start with A ?
#q17 print other name of country ? // its given from user
#q18 print all region of countries ?


from json import load
f=open("/Users/shameershajahan/Desktop/PythonJune/jsonWorks/countries.json")
country=load(f)




# // q1  print all the country in the list ?

all_country=[ac for ac in country ]
# print(len(all_country))




# // q16 print all names start with A ?


# name=[c.get("name") for c in country ]
# start=[st for st in name if st.startswith("A")]
# print(start)




# // q17 print other name of country ? // its given from user

# country_name=input("Enter the name \n")


# //  print all region of countries ?

all_regions = {c.get("region") for c in country}
# print(all_regions)






region_summery={}

for c in country:

    region_name=c.get("region")

    if region_name in region_summery:

        region_summery[region_name]+=c.get("area",0)

    else:

        region_summery[region_name]=c.get("area",0)


value_key=[(v,k) for k,v in region_summery.items()] 

print(max(value_key))