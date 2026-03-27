# list is a mutable squence of value .. we create list like this []
        
marks = [91,32,43,235,454,2,34]

print(marks[:])


# appending
marks.append(6)

print(marks)

# inserting at pos
marks.insert(-1,555)

print(marks)

# sorting
# for assending and for descending order user marks.sort(reverse=True) 
marks.sort()

print(marks)
#reverse
marks.reverse()