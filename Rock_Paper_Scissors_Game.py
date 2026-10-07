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
choice = int(input("What do you choose (Rock = 0 ,Paper = 1 ,Scissors = 2)?\n"))
game_pic = [rock, paper, scissors]
if choice >= 0 and choice <= 2:
    print(game_pic[choice])
else:
    print('You lose! (You wrote an invalid number !)')
computer = random.randint(0, 2)
print('Computer choice :')
print(game_pic[computer])
if choice == computer:
    print('It\'s a draw!')
elif (choice == 2 and computer == 0) or (choice < computer):
    print('You lose!')
elif (choice == 0 and computer == 2) or (choice > computer):
    print('You win!')
