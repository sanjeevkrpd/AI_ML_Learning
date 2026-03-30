list_1 = [9, 2, 4, 5, 2, 8]
list_2 = [0, 4, 5, 3, 8, 7]

# Step 1: Sort both lists
list_1 = sorted(list_1)
list_2 = sorted(list_2)

# Step 2: Merge logic
i = 0
j = 0
list_3 = []

while i < len(list_1) and j < len(list_2):
    if list_1[i] < list_2[j]:
        list_3.append(list_1[i])
        i += 1
    else:
        list_3.append(list_2[j])
        j += 1

# Step 3: Add remaining elements
while i < len(list_1):
    list_3.append(list_1[i])
    i += 1

while j < len(list_2):
    list_3.append(list_2[j])
    j += 1

# Final Output
print("Merged Sorted List:", list_3)