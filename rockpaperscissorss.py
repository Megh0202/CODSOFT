import random

def get_computer_choice():
    """Generate and return the computer choice."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the game rules."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Function to play a single round of Rock-Paper-Scissors."""
    print("Welcome to Rock-Paper-Scissors!")
    # Score tracking
    user_score = 0
    computer_score = 0
    while True:
        print("\nChoose one: rock, paper, or scissors.")
        user_choice = input("Your choice: ").lower()
        # Input validation
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        # Determine the winner of the round
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        print(f"Score: You - {user_score}, Computer - {computer_score}")
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Final score:")
            print(f"You - {user_score}, Computer - {computer_score}")
            break

if __name__ == "__main__":
    play_game()
