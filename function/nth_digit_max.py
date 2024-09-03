


def nth_digit_max(num1,num2):
    cal=num1%10 #3
    min=num2%10
    return num1 if cal>=min else num2
    # if(cal<=min):
    #     return num2
    # else:
    #     return num1
    
print(nth_digit_max(234,752))


