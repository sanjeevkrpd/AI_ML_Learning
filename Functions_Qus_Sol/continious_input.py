
def print_until_quit():
     
    while(True):
        value = input("Enter any no : ")
        if(value == "Quit"):
            break
        no = int(value)            
        if(no > 0):
            print("No is Positive")
            
        else:
            print("No is Negative")
                        
print_until_quit()                        