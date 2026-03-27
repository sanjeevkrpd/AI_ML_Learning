
def count_no_digits(no):
    count = 0
    while(no != 0):
        count +=1
        no = int (no/10)
    return count

print(count_no_digits(312))        
        