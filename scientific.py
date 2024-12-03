import tkinter as tk
from tkinter import messagebox
import math

# Function to handle basic operations
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
            screen.update()
    elif text == "C":
        screen_var.set("")
        screen.update()
    else:
        screen_var.set(screen_var.get() + text)
        screen.update()

# Function for scientific operations
def scientific_operation(operation):
    try:
        value = float(screen_var.get())
        if operation == "sqrt":
            result = math.sqrt(value)
        elif operation == "log":
            result = math.log(value)
        elif operation == "sin":
            result = math.sin(math.radians(value))
        elif operation == "cos":
            result = math.cos(math.radians(value))
        elif operation == "tan":
            result = math.tan(math.radians(value))
        screen_var.set(str(result))
    except ValueError:
        screen_var.set("Error")

# GUI Setup
root = tk.Tk()
root.title("Professional Scientific Calculator")
root.geometry("400x550")
root.config(bg="#222831")

# Screen display for input and output
screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font=("Arial", 24), bd=10, insertwidth=4, width=15, borderwidth=6, relief=tk.RIDGE)
screen.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# Button layout and styling
button_config = {
    'font': ('Arial', 18),
    'bg': '#949393',
    'fg': '#FFFFFF',
    'relief': tk.RAISED,
    'bd': 4,
    'padx': 15,
    'pady': 10,
    'activebackground': '#949393',
    'activeforeground': '#EEEEEE'
}

scientific_buttons_config = {
    'font': ('Arial', 16),
    'bg': '#949393',
    'fg': '#EEEEEE',
    'relief': tk.RAISED,
    'bd': 4,
    'padx': 10,
    'pady': 10,
    'activebackground': '#949393',
    'activeforeground': '#FFFFFF'
}

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    ".", "0", "=", "+"
]

# Adding basic buttons to the GUI
row, col = 1, 0
for button in buttons:
    btn = tk.Button(root, text=button, **button_config)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    btn.bind("<Button-1>", click)
    col += 1
    if col == 4:
        col = 0
        row += 1

# Adding scientific buttons to the GUI
scientific_buttons = [
    ("sqrt", "√"), ("log", "log"), ("sin", "sin"), ("cos", "cos"), ("tan", "tan")
]

for i, (operation, label) in enumerate(scientific_buttons):
    btn = tk.Button(root, text=label, **scientific_buttons_config)
    btn.grid(row=row, column=i, padx=5, pady=5, sticky="nsew")
    btn.config(command=lambda op=operation: scientific_operation(op))

# Clear button
clear_btn = tk.Button(root, text="C", font=("Arial", 18), bg="#949393", fg="#FFFFFF", relief=tk.RAISED, bd=4, padx=20, pady=10, activebackground="#949393", activeforeground="#FFFFFF")
clear_btn.grid(row=row+1, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
clear_btn.bind("<Button-1>", click)

# Configure grid weight for responsive resizing
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(row + 2):
    root.grid_rowconfigure(i, weight=1)

# Start the main loop
root.mainloop()
