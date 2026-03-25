auth_user = "admin"
auth_pass = "admin@123"

user_name = input("Enter username : ")
password= input("Enter password : ")

if auth_user == user_name:
    if auth_pass == password:
        print("login successfully")
    else:
        print("password is wrong")
else:
    print("user name is wrong")