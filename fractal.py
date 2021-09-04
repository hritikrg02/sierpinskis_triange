"""
file: fractal.py
description: draws sierpinski's triangle at specified user level
language: python3
author: Hritik "Ricky" Gupta
"""

import turtle as t
from random import randint

PEN_WIDTH = 1
SIDE_LEN = 1150

def init():
    """
    initializes the turtle
    """
    t.up()
    t.colormode(255)
    t.pensize(PEN_WIDTH)
    t.tracer(False)
    t.setposition(0, -480)
    t.down()

def draw_triangle(side):
    """
    draws a single triangle
    """
    t.down()
    t.forward(side/2)
    t.left(120)
    t.forward(side)
    t.left(120)
    t.forward(side)
    t.left(120)
    t.forward(side/2)
    t.up()

def fractal_rec(side, depth):
    """
    draws a recursive triangle fractal
    :param side: sidelength
    :param depth: how many recursions should occur
    """
    if depth == 0:
        pass
    else:
        draw_triangle(side)

        t.forward(side/4)
        #t.color(randint(0, 255), randint(0, 255), randint(0, 255))
        fractal_rec(side/2, depth-1)

        t.forward(side/4)
        t.left(120)
        t.forward(side)
        t.left(120)
        t.forward(side/2)
        t.left(120)
        t.forward(side/4)
        fractal_rec(side/2, depth-1)

        t.forward(side/4)
        t.left(120)
        t.forward(side/2)
        t.left(120)
        t.forward(side)
        t.left(120)
        t.forward(side/4)
        fractal_rec(side/2, depth-1)

        t.forward(side/4)

def main():
    """
    initializes the program and draws as many levels as the user desires
    """
    depth = int(input("How many levels? "))
    init()
    fractal_rec(SIDE_LEN, depth)
    t.tracer(True)
    t.hideturtle()
    t.done()

if __name__ == '__main__':
    main()
