import random

random_integer = random.randint(1,20)

if random_integer == 20:
    print(f"You rolled a {random_integer}! This is a critical hit!")
elif random_integer == 1:
    print(f"You rolled a {random_integer}! This is a critical failure!")
else:
    print(f"You rolled a {random_integer}.")

    