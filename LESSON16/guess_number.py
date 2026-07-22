from random import choice
from sys import exit

def guess_game(name="PlayerOne"):
    count = 0
    player_wins = 0
    computer_wins = 0

    def guess_number():
        nonlocal name
        player_choice = input(f"\n\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n")
        
        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return guess_number()
        
        computer_choice = choice("123")
        player = int(player_choice)
        computer = int(computer_choice)

        print(f"\n{name}, you chose {player}.\nI was thinking about the number {computer}.\n\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            
            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                computer_wins += 1
                return f"Sorry, {name}. Better luck next time. 😢"

        result = decide_winner(player, computer)
        
        nonlocal count
        nonlocal player_wins
        nonlocal computer_wins

        count += 1
        
        print(result)
        print(f"\nGame count: {count} \n\n")
        print(f"{name}'s Wins: {player_wins} \n\n")
        print(f"Computer Wins: {computer_wins} \n\n")
        print(f"Your winning percentage: {player_wins/count:.2%}\n\n")

        while True:
            play_again = input(f"Play again, {name}? \n\nY for yes or \nQ to quit\n\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break
        
        if play_again == "y":
            return guess_number()
        else:
            if __name__ == "__main__":
                print("\n🎉🎉🎉🎉")
                print("Thank you for playing!\n")
                exit(f"Bye {name}! 👋")
            else:
                return

    return guess_number

if __name__ == "__main__":

    import argparse

    paser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    paser.add_argument(
        "-n", "--name", metavar="name", required=True,
        help="The name of the person playing the game."
    )

    args = paser.parse_args()
    
    play_guess_game = guess_game(args.name)
    play_guess_game()