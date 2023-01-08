#Rock paper scissors game against the computer
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_images = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
print(game_images[player_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])
if player_choice >= 3 or player_choice < 0:
    print("Choose a number between 0 and 2")

if player_choice == computer_choice:
    print("It's a draw.")
elif (player_choice == 0 and computer_choice == 1):
    print("Computer wins. YOU LOSE :(")
elif (player_choice == 1 and computer_choice == 2):
    print("Computer wins. YOU LOSE :(")
elif (player_choice == 2 and computer_choice == 0):
    print("Computer wins. YOU LOSE :(")
elif (player_choice == 1 and computer_choice == 0):
    print("You Win!!!")
elif (player_choice == 2 and computer_choice == 1):
    print("You Win!!!")
elif (player_choice == 0 and computer_choice == 2):
    print("You Win!!!")
