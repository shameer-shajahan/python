
# //  function in regularexpression //


# finditer
# fullmatch





from re import finditer


text="abBcgn,-+ 123 @# $efg"

# pattern="[ab g]"      #      // check for either a,b," ",g also print
# pattern="[A-K]"       #     // to check all uppercase letter from A to K
# pattern="[a-k]"       #    // to check all lowercase letter from A to K
# pattern="[A-Za-z]"    #   // to check lower and upper case alphabets
# pattern="[0-9]"       #  // to check digit from 1 to 9 
# pattern="[a-zA-z0-9]" #   // to check both alphanumeric characters
# pattern="[^a-zA-Z]"   #     // to check  is_alphabets 
# pattern="[\s]"        #       // to check only space characters
pattern="[^a-zA-Z\s]"   #         // to check only space characters

maches=finditer(pattern,text)

for m in maches:

    print(m.start(),"==",m.group())





# special patterns


# \s  # [space]
# \s  # [^space]
# \d  # [0-9]
# \D  # [^0-9]
# \w  # [  alphanumeric]
# \W  # [ ^ alphanumeric]


# {2} only two
# {1,4} minumum o1 or maximum 

# + match one or more
# ? optional
# - zero or more
# . selective