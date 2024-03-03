
#####THIS IS FOR https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#####Will complete the map in under 300 steps. Will work to refine it down more.


def turn_right():
    turn_left()
    turn_left()
    turn_left() 
def wall_in_front_move():
    while wall_in_front() == True:
        if wall_on_right():
            turn_left()
        else:
            turn_right()
    move()

while not at_goal():
    if wall_in_front() and wall_on_right():
        wall_in_front_move()
    elif right_is_clear() and front_is_clear():
        turn_right()
        move()
    elif wall_in_front() and right_is_clear():
        turn_right()
        move()
    elif front_is_clear() and right_is_clear() and is_facing_north():
        move()
    else:
        move()