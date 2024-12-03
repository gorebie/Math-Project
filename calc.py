import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Define the expression variable to store input
expression = ""

# Function to update the expression in the entry box
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total  # Continue from the result
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the input
def clear():
    global expression
    expression = ""
    equation.set("")

# Define the main window size
window.geometry("400x500")

# Create a string variable to hold the equation
equation = tk.StringVar()

# Create an entry box for the calculator display
entry_box = tk.Entry(window, textvariable=equation, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=4)
entry_box.grid(row=0, column=0, columnspan=4)

# Create buttons for the calculator
button_list = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]

# Define the row and column for each button
row_value = 1
col_value = 0

# Add buttons dynamically using a loop
for button_text in button_list:
    if button_text == "=":
        button = tk.Button(window, text=button_text, font=("Arial", 18), height=2, width=5, bd=4,
                           command=equalpress)
    else:
        button = tk.Button(window, text=button_text, font=("Arial", 18), height=2, width=5, bd=4,
                           command=lambda btn=button_text: press(btn))

    button.grid(row=row_value, column=col_value)

    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Clear button
clear_button = tk.Button(window, text='C', font=("Arial", 18), height=2, width=5, bd=4, command=clear)
clear_button.grid(row=row_value, column=0, columnspan=4)

# Run the application
window.mainloop()
