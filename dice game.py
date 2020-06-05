import random
min = 1
max = 6
roll_again = "y"
while roll_again is  "y":
    print("rolling the dices...")
    print("the values are")
    print(random.randint(min,max))
    print(random.randint(1,6))
    roll_again = input("roll the dices again? ")
    