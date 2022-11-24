print("The final ex of day 3")

answer = input("Where do you go? Left of right? ")
answer = answer.lower()
if answer == "left":
    print("The game if over")
else:
    answer = input("Now you are on the lake. Do you want to swim or wait for a boat? Swim/Boat: ")
    answer = answer.lower()
    if answer == "swim":
        print("The game is over")
    else:
        answer = input("Now you have 3 doors: Blue, Yellow or Red: ")
        answer = answer.lower()
        if answer == "yellow":
            print("You find the out. You win")
        elif answer == "red":
            print("You are on the fire. You lost")
        else:
            print("You was died. You lost")