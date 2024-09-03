

arr=[[10,30],[12,30],[40,90]]

evens=[num for lst in arr for num in lst if num%2==0]
print(sum(evens))