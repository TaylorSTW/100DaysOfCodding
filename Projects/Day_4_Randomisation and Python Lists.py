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

choise_player = int(input("Put the number 0 - rock, 1 - paper, 2 - scissors\n"))
list_choise = [rock, paper, scissors]
computer = random.randint(0, 2)
if computer == choise_player:
    print(f"{list_choise[choise_player]}\n{list_choise[computer]}\n\nHere are not winner")
else:
    if choise_player == 0 and computer == 1:
        print(f"{list_choise[choise_player]}\n{list_choise[computer]}\n\nYou are lost")
    elif choise_player == 0 and computer == 2:
        print(f"{list_choise[choise_player]}\n{list_choise[computer]}\n\nYou are win")
    elif choise_player == 1 and computer == 0:
        print(f"{list_choise[choise_player]}\n{list_choise[computer]}\n\nYou are win")
    elif choise_player == 1 and computer == 2:
        print(f"{list_choise[choise_player]}\n{list_choise[computer]}\n\nYou are lost")
    elif choise_player == 2 and computer == 1:
        print(f"{list_choise[choise_player]}\n{list_choise[computer]}\n\nYou are win")
    else:
        print(f"{list_choise[choise_player]}\n{list_choise[computer]}\n\nYou are lost")