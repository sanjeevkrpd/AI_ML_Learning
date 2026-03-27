
def sum_of_digit(n):
    sum=0
    while(n != 0):
        rem = n%10
        sum += rem
        n =  int (n /10)
    return sum

print(sum_of_digit(312))     
        