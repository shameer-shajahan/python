def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

lst=[10,20]

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)