from random import randint

num_dice = int(input("How many dice are we rolling? "))
num_sides = int(input("How many sides on each die? "))

while True:
    for i in range(num_dice):
        result = "|"
        side_random = randint(1, num_sides)
        result += f"{side_random}"
        print(result)
    roll_again = input("Roll again? ('q' to quit) ")
    if roll_again == 'q':
        break




