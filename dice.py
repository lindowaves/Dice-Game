import random

dice_set = {
    1:("┌─────────┐\n"
       "|         |\n"
       "|    ●    |\n"
       "|         |\n"
       "└─────────┘\n"),

    2:("┌─────────┐\n"
       "|  ●      |\n"
       "|         |\n"
       "|      ●  |\n"
       "└─────────┘\n"),

    3:("┌─────────┐\n"
       "|  ●      |\n"
       "|    ●    |\n"
       "|      ●  |\n"
       "└─────────┘\n"),

    4:("┌─────────┐\n"
       "|  ●   ●  |\n"
       "|         |\n"
       "|  ●   ●  |\n"
       "└─────────┘\n"),

    5:("┌─────────┐\n"
       "|  ●   ●  |\n"
       "|    ●    |\n"
       "|  ●   ●  |\n"
       "└─────────┘\n"),

    6:("┌─────────┐\n"
       "| ●  ●  ● |\n"
       "|         |\n"
       "| ●  ●  ● |\n"
       "└─────────┘\n")
}

def roll_dice(num):
    dice_numbers = [1,2,3,4,5,6]

    if num in dice_numbers:
        for die in range(num):
            roll = random.randint(1,6)
            print(dice_set[roll], end="  ")
            print()
    else:
        print("Please enter a number between [1-6]")
        SystemExit(1)

user_dice = int(input("Enter a number of dice [1-6]: "))
roll_dice(user_dice)