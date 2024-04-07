import random
import time

def display_choices():
    print("Available choices:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

def get_user_choice():
    choice = int(input("Enter your choice (1-3): "))
    choices = ['Rock', 'Paper', 'Scissors']

    if choice < 1 or choice > 3:
        print("Invalid choice. Please choose a number between 1 and 3.")
        return None

    return choices[choice - 1]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", "tie"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!", "user"
    else:
        return "You lose!", "computer"

def display_result(user_choice, computer_choice, result):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(f"Result: {result}")

def play_game():
    display_choices()
    user_choice = get_user_choice()

    if user_choice is None:
        return

    print("Rock...")
    time.sleep(1)
    print("Paper...")
    time.sleep(1)
    print("Scissors...")
    time.sleep(1)

    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    print("Computer's choice is made!")
    print()

    result_message, winner = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result_message)

    return winner

if _name_ == "_main_":
    user_score = 0
    computer_score = 0

    while True:
        print("Welcome to Rock, Paper, Scissors!")
        winner = play_game()

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Final score:")
            print(f"You: {user_score}, Computer: {computer_score}")
            break