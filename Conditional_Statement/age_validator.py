age = int(input("Enter your age : "))

if age < 13 :
    print("you are a child")
elif age > 13 and age < 18:
    print("you are a teenager")
elif age >= 18:
    print("you are an aduld")
else:
    print("not match")  