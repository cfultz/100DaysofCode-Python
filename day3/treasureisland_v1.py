print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
print(" ")
#### Start game ###


crossroad = str(input("You're at a cross road. Where do you want to go? Type 'left' or 'right': "))
if crossroad == str("right"):
    print("You start to walk down the right facing path. You come upon a group of thugs that beat you and take your belongings. You died.")
elif crossroad == str("left"):
    shore = str(input("You find yourself at the waters edge. You see an island in the lake. Type 'swim' go to island now or 'wait' to wait for a boat: "))
    if shore == str("swim"):
        swim = print("You swim 20 meters into the water when from below the depths, a lake serpent attacks you. You died.")
    elif shore == str("wait"):
        island = str(input("You arive at the island safely. You see two houses, one red and the other blue. Which do you enter? Type 'red' or 'blue': "))
        if island == str("red"):
            print("You enter the house. As you close the door, you smell a faint whiff of petrol. As the door clasps shut, the room sets ablaze. You cannot escape and are engulfed in fire. You died.")
        elif island == str("blue"):
            print("You enter the house. As you close the door, the room becomes dark. In the corner, there is a shining blue glow. As you get closer, you realize it\'s a chest. You found the treasure!")
else:
    print("You are not ready to explore for treasure if you can\'t follow directions.")