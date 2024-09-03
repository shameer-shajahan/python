# write to print to find the monthly emi with intrest ?

amount=200000
intrest=9
year=10

# //EMI = P * r * (1 + r)**n / (1 + r)**n - 1
# p = loan amount
# r = intrest rate
# n = month
p=amount
print(amount)
# convert annual intrest rate into monthly interest rate
r=intrest/100/12
print("intrest rate =",r)

# convert year to month
n=year*12
print(f"months ={n}")

emi=((p)*(r)*((1+r)**n))/(((1+r)**n)-1)
print(emi)

# total amount of pay loan
total_amount=emi*n
print("total amount of payment in loan",total_amount)

# total amount of intrest loan
total_intrest=total_amount-p
print("total amount of intrest in loan",total_intrest)