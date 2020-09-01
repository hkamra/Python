try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import math

# def parabola(x):
#     y = x * x / 100
#     return y


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)   # this is the positive x-axis
        plot(page, -x, y)  # this is the negative x-axis


# Mini Challenge
# Modify the circle function so that it allows the colour of the circle to be specified
# and defaults to red if a colour is not given. You may want to review the previous lectures
# about named parameters and default values.
# My solution:- add a parameter in the function circle and initialised as "red", now if
# the argument is passed in the function call for the colour it will pass that colour to the function
# else it will display the colour "red" as default


def circle(page, radius, g, h, colour="red"):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=2)
    # for x in range(g * 100, (g + radius) * 100):    # multiply by 100 is to scale up
    #     x /= 100                                    # scale down in order to use the original value
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))  # lecture 192
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())  # this is to display local variables used in this function


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# below is dividing the canvas into 2
# canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="blue")
# canvas2.grid(row=0, column=1)
#
# print(repr(canvas), repr(canvas2))  # repr shows the memory address where canvas is stored
# draw_axes(canvas2)
draw_axes(canvas)

# function within a class are called methods, for ex:- Canvas

parabola(canvas, 100)
parabola(canvas, 200)
# below code is commented out in order to avoid execution time halt due to scale up the circle function
circle(canvas, 100, 0, 0)
circle(canvas, 200, 0, 0)
circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100)
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0, colour="blue")  # solution to mini challenge

mainWindow.mainloop()
