#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
# x = 20/0
# print(x)
# TODO: Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
try:
    x = 20 / 0

except:
    print("Math Error")

# TODO: You can also catch specific exceptions
