def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# def centre_text(text):           # parameter is the variable in the function definition
#     text = str(text)             # this will avoid the error if string is not passed as an argument
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text)


# below is the updated centre_text function
# asterisk in the parameter means multiple input parameters, same as print fx
# in python function call doesn't need to have arguments for all the parameters
# def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
#     # text = " ".join(args)       # this only works if the parameter only contains string
#     text = ""
#     for arg in args:
#         text += str(arg) + sep
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text, end=end, file=file, flush=flush)
#
#
# with open("centred", mode='w') as centred_file:
#
#     centre_text("spam and eggs", file=centred_file)     # argument is the actual value passed in the function
#     centre_text("spam, spam and eggs", file=centred_file)
#     centre_text(12, file=centred_file)                  # this will give an error
#     centre_text("spam, spam, spam and eggs", file=centred_file)
#
#     centre_text("first", "second", 3, 4, "spam", sep=":", file=centred_file)


########################
# Use of return method #
########################
def centre_text(*args, sep=' '):
    # text = " ".join(args)       # this only works if the parameter only contains string
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


with open("menu", 'w') as menu:
    s1 = centre_text("spam and eggs")
    print(s1, file=menu)
    s2 = centre_text("spam, spam and eggs")
    print(s2, file=menu)
    print(centre_text(12), file=menu)
    print(centre_text("spam, spam, spam and eggs"), file=menu)
    s5 = centre_text("first", "second", 3, 4, "spam", sep=":")
    print(s5, file=menu)
