def is_leap(year):
    # Check if the year is divisible by 400
    if year % 400 == 0:
        return True
    # Check if the year is divisible by 100 but not by 400
    elif year % 100 == 0:
        return False
    # Check if the year is divisible by 4 but not by 100
    elif year % 4 == 0:
        return True
    # For all other cases, it is not a leap year
    else:
        return False
