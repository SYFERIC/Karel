"""
File: DoubleBeepers.py
Name:Eric Shih
-------------------------------

"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double()
    move()
    turn_back()
    back()
    move()
    move()
    turn_back()


def double():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_back()
        move()
        turn_back()

def turn_back():
    turn_left()
    turn_left()

def back():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        turn_back()
        move()
        turn_back()















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)