

number=[11,4,3,6,10,5,2] 

# // logic 1

# largest_number=0

# second_largest=0 

# for i in number:
    
#     if i > largest_number and i > second_largest  :
        
#         second_largest=largest_number

#         largest_number=i

#     elif i > second_largest and i < largest_number:


#         second_largest=i


# print(f"second largest number = {second_largest}")



# // logic 2

number.sort()

print(number[-2])




