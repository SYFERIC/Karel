"""
File: Steeplechase.py
Name: Eric Shih
---------------------------------

"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """

    """
    move()
    up()
    cross()
    down()
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            up()
            cross()
            down()



def up():
    while not front_is_clear():
        turn_left() #Karel is Facing North
        move()
        turn_right()
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def cross():
    move()
    turn_right()


def down():
    while front_is_clear():
            move()
    turn_left()
















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
