# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter
import os

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('240x320-8-200')
mainWindow['padx'] = 8

# mainWindow.columnconfigure(0, weight=1000)
# mainWindow.columnconfigure(1, weight=1000)
# mainWindow.columnconfigure(2, weight=1000)
# mainWindow.columnconfigure(3, weight=1000)
# mainWindow.columnconfigure(4, weight=1000)
# mainWindow.columnconfigure(5, weight=1000)
# mainWindow.rowconfigure(0, weight=1000)
# mainWindow.rowconfigure(1, weight=1000)
# mainWindow.rowconfigure(2, weight=1000)
# mainWindow.rowconfigure(3, weight=1000)

# widget to display the result
# resultLabel = tkinter.Label(mainWindow)
# resultLabel.grid(row=0, column=0, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

calculator_numbers = [["C", "CE"],
                      ["7", "8", "9", "+"],
                      ["4", "5", "6", "-"],
                      ["1", "2", "3", "*"],
                      ["0", "=", "/"]
                      ]

# Buttons
# for i in calculator_numbers:
#     for j in i:
#         list_buttons = tkinter.Button(mainWindow, text=j)
#         list_buttons.grid(row=calculator_numbers.index(i), column=j.index(j), sticky='w')

buttonsLabel = tkinter.Label(mainWindow)
buttonsLabel.grid(row=1, column=0, sticky='nw', columnspan=4)

for i in range(5):
    for j in range(4):
        if (i == 0 and (j == 2 or j == 3)) or (i == 4 and j == 3):
            # do nothing
            continue
        # elif j != 0:
        #     list_buttons = tkinter.Button(buttonsLabel, text=calculator_numbers[i][j])
        #     list_buttons.grid(row=i, column=j, sticky='e')
        else:
            list_buttons = tkinter.Button(buttonsLabel, text=calculator_numbers[i][j])
            list_buttons.grid(row=i, column=j, sticky='ew')  # sticky is to expand the key in e and w

mainWindow.mainloop()
