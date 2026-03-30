list_1 = {1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20}
even_list = []
odd_list = []

for i in list_1:
    if(i % 2 == 0):
        even_list.append(i)
    else:
        odd_list.append(i)

print("------- even list ------------")
print(even_list)
print("------- odd list ------------")
print(odd_list)
