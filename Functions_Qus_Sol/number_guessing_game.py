import random

def start_game(max_val):
    print("Ok Lets Go... To Play Number Guessing 🎯")
    
    while True:
        no = random.randint(1, max_val)  
        
        while True:
            try:
                guess = int(input("Enter the number to guess: "))
            except ValueError:
                print("❌ Please enter a valid number")
                continue

            if guess > no:
                print(guess, "- your guessing is too high ⬆️")
            elif guess < no:
                print(guess, "- your guessing is too low ⬇️")
            else:
                print(guess, "=", no)
                print("🎉 Booyah! You nailed it!")
                break  
        
        user_value = input("Type 'start' to play again or 'quit' to exit: ").lower()
        
        if user_value != "start" and user_value != "":
            print("👋 Thanks for playing!")
            break



val = int(input("Enter the max number you want to play with: "))
start_game(val)