# Program description goes here
# Updated on:
# Updated by:
#
#
# imports the tkiner library which is used to create a GUI
from tkinter import *

# This crates the main window.
root = Tk()

# Names the window simple calculator.
root.title("Simple Calculator")

# Entry widget where users can input numbers or results. 
# The width is set to 35 characters, with a border width of 5.
# The grid method places it in the first row, first column across 3 columns.
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# # Function that is triggered when a number button is pressed.
# It gets the current content in the input and deletes it.
# And appends the clicked number at the end of the input.
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# # Defines the function for entry widget to clear when pressed
def button_clear():
    e.delete(0, END) # Deletes all the content in the entry widget

# Document what the following lines of code do here
# This function works by  pressing an operator button that  stores the first operand (the number) and the operator, then is
# ready to proceed to the next operand or action.
def button_operator(operator):
    first_number = e.get()
    global f_num
    global num_operator
    f_num = int(first_number)
    num_operator = operator
    e.delete(0, END)

# Document what the following lines of code do here
# This function takes two numbers (one from the entry field and one stored in f_num), 
# applies the selected arithmetic operation (based on num_operator), 
# and displays the result in the entry field.# If the operator is not recognized, it shows "Invalid!!!".
# you might want to consider adding documentation on a line by line basis since
# this is a critical function for the program
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if num_operator == '+':
        e.insert(0, f_num + int(second_number))
    elif num_operator == '*':
        e.insert(0, f_num * int(second_number))
    elif num_operator == '/':
        e.insert(0, f_num / int(second_number))
    elif num_operator == '-':
        e.insert(0, f_num - int(second_number))
    else:
        e.insert(0, "Invalid!!!")

# Document what the following lines of code do here
# This code sets up the graphical interface for a calculator with buttons for the numbers 0-9, 
# an addition operator (+), an equals button (=), and a clear button (Clear). 
# The actual behavior and calculations depend on how the button_click, button_operator,
# button_equal, and button_clear functions are implemented elsewhere in the program.

# NOTE: We did not cover Lambda functins in class. A Lambda Function 
# in Python programming is an anonymous function
# or a function having no name. It is a small and restricted function 
# having no more than one line. In the case below, the Lambda function code
# is calling the code/function button_click() with the numbers 0-9 as the 
# parameter. Just like a normal function, a Lambda function can have multiple
# arguments with one expression. 

button_1 =  Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 =  Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 =  Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 =  Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 =  Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 =  Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 =  Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 =  Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 =  Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 =  Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add =  Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))
button_equal =  Button(root, text="   =   ", padx=79, pady=20, command=button_equal)
button_clear =  Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Document what the following lines of code do here
# It creates three buttons for subtraction (-), multiplication (*), and division (/), each with specific padding for appearance. 
# When any of these buttons are clicked, they will call the button_operator function,
# passing the respective operator ("-", "*", or "/") as an argument, 
# which will likely be used to perform the corresponding operation in the calculator program.
# See the description of a Lambda function above
button_subtract =  Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
button_multiply =  Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
button_divide =  Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))

# Document what the following lines of code do here
# This grid layout creates a basic calculator interface, where number buttons (0-9) and mathematical operators (addition, subtraction, multiplication, division) are arranged logically. 
# The button_clear and button_equal buttons perform specific functions like clearing the input or showing the result, respectively.

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# Document what the following line of code do here
#this code call upoon the mainloop function
root.mainloop()
