

# number=[1,2,[3,(100,200,300),4],5,6] >>> [1,2,[3,4,(100,150,200,300)],5,6]

number=[1,2,[3,(100,200,300),4],5,6]

num=number[2][1]

new_num=list(num)

new_num.append(150)
 
new_num.sort()

# print(tuple(new_num))

number[2][1]=tuple(new_num)

va=number[2].pop()

number[2].insert(1,va)

print(number)


