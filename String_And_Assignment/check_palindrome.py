

def check_palindrome(user_val):
    left = 0
    right = len(user_val) -1
    while(left < right):
        if(user_val[left] != user_val[right]):
            return False    
        left +=1
        right-=1
        
        return True

user_val = input("Enter Any String : ")

print(check_palindrome(user_val))



    