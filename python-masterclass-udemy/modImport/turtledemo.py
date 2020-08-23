# import turtle
# # import time
# # from turtle import forward         # this is to only import specific methods class from turtle module
# from turtle import forward, right, done, circle
#
# # if only specific functions are used from module, we don't need to use turtle command
# forward(150)
# right(250)
# forward(150)
# turtle.circle(75)
#
# done()

# this is the turtle game from 1960 in which kids use to give commands to turtle and it draws line
# turtle.forward(150)
# turtle.right(250)
# turtle.forward(150)
#
# # time.sleep(4)
# turtle.done()       # this will keep the graphics window open until we close it


################################################################################
from turtle import *                     # avoid this way, this imports everything, as we don't know what classess
# it's importing

done_message = "Well done you have finished your drawing"

forward(150)
right(250)
forward(150)
circle(75)

done()
print(done_message)     # this will give an error, as the user doesn't know that done keyword is imported above and
# and cannot be used as a variable name. Unless it's changed to something else to avoid error

