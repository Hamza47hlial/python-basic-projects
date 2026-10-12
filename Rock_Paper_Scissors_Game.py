import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)  (Rock)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)  (Paper)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)  (Scissors)
      (____)
---.__(___)
'''

# The list position matches the number: 0 = rock, 1 = paper, 2 = scissors
game_pic = [rock, paper, scissors]
names = ["Rock", "Paper", "Scissors"]

# Each key BEATS its value: rock (0) beats scissors (2),
# paper (1) beats rock (0), scissors (2) beat paper (1)
beats = {0: 2, 1: 0, 2: 1}


def get_choice():
    """Keeps asking until the user types 0, 1 or 2."""
    while True:
        try:
            choice = int(
                input("What do you choose (Rock = 0, Paper = 1, Scissors = 2)?\n"))
        except ValueError:
            print("That's not a number, try again.")
            continue
        if 0 <= choice <= 2:
            return choice
        print("Please type 0, 1 or 2.")


def play_round():
    """Plays one round and returns 'win', 'lose' or 'draw'."""
    choice = get_choice()
    computer = random.randint(0, 2)

    print(f"\nYou chose {names[choice]}:")
    print(game_pic[choice])
    print(f"Computer chose {names[computer]}:")
    print(game_pic[computer])

    if choice == computer:
        print("It's a draw!")
        return "draw"
    elif beats[choice] == computer:
        print("You win!")
        return "win"
    else:
        print("You lose!")
        return "lose"


wins = losses = draws = 0

# Keep playing rounds until the user says no
while True:
    result = play_round()
    if result == "win":
        wins += 1
    elif result == "lose":
        losses += 1
    else:
        draws += 1

    print(f"Score -> Wins: {wins} | Losses: {losses} | Draws: {draws}")

    again = input("\nPlay again? Type 'y' or 'n' : ").lower()
    # If the user types anything other than "y" it will stop
    if again != "y":  
        print("Thanks for playing!")
        break
