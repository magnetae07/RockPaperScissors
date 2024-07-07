import random
#getting the computer's choice

def get_computer_choice():
    choices = ["rock","paper", "scissors"]
    return random.choice(choices)

#getting the player's choice

def get_player_choice():
    choices = ["rock", "paper", "scissors"]
    while True:
        player_choice=input("Enter rock, paper, or scissors: ").lower()
        if player_choice in choices:
            return player_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

# finding the winner

def find_winner(player_choice, computer_choice):
    if player_choice==computer_choice:
        return "tie"
    elif (player_choice=="rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
        return "player"
    else:
        return "computer"

# displaying the result

def display_result(player_choice, computer_choice, winner):
    if winner == "tie":
        print(f"Both chose {player_choice}. It's a tie!")
    elif winner == "player":
        print(f"Player chose {player_choice}, computer chose {computer_choice}. Player wins!")
    else:
        print(f"Player chose {player_choice}, computer chose {computer_choice}. Computer wins!")

def rock_paper_scissors():
    computer_choice=get_computer_choice()
    player_choice=get_player_choice()
    winner = find_winner(player_choice,computer_choice)
    display_result(player_choice,computer_choice,winner)

# running the game
if __name__ == "__main__":
    rock_paper_scissors()
