
name=set()
name={"new"}
name.add("hi") # // to add element in a set
# print(name)

# name.clear  # // to clear all elements in a set
# print(name)

name.add("kochi")
# name.pop()   # // to remove a randam element in a set 
# print(name)

# name.discard("kochi") # // to remove a specific element in a set
# print(name)


new_name=["lenovo","mac","dell","hi","new"]
# name.update(new_name)       # // to add element from any collection of set
# print(name)




        # Important methods

        # 1. union()
        # 2. intersection()
        # 3. difference()


# new_set=name.union(new_name) # // to return the combined element from two sets and return as a new set
# print(new_set)


# intersection=name.intersection(new_name) # // to return commen element from two set object as a new set
# print(intersection)


# difference=name.difference(new_name)  # // TO return element from set name which not in second set 
# print(difference)


symetric_differenc=name.symmetric_difference(new_name)
print(symetric_differenc)