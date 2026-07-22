import sys
from guess_number import guess_game
from rps import rps


def play_arcade(name="PlayerOne"):
    playerchoice = input(
                f'\n{name}, welcome to the Arcade! 🤖  \n\nPlease choose a game: \n1 = Rock Paper Scissors,\n2 = Guess My Number\n\n Or press "x" to exit the Arcade\n\n')
        
    if playerchoice not in ["1", "2", "x"]:
        return play_arcade(name)

    if playerchoice == "1":
        play_rps = rps(name)
        play_rps()
        return play_arcade(name)
    elif playerchoice == "2":
        play_guess_game = guess_game(name)
        play_guess_game()
        return play_arcade(name)
    else:
        sys.exit(f"See you next time, {name} \nThanks for Playing 👋👋👋")



        


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

    play_arcade(args.name)
  

