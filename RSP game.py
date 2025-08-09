import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissor"])

def get_user_choice():
    choice = input("Enter your choice (rock/paper/scissor): ").lower()
    while choice not in ["rock", "paper", "scissor"]:
        print("Invalid choice!")
        choice = input("Enter your choice (rock/paper/scissor): ").lower()
    return choice

def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "rock" and computer == "scissor") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissor" and computer == "paper"):
        return "User wins!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(f"Result: {result}")

# Run the game
play_game()
