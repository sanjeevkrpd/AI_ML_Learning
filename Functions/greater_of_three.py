
def greater(a,b,c):
    if a > b and b > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    


print(greater(11,9,22))    