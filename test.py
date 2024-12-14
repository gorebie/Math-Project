import tkinter as tk
 
master_window = tk.Tk()
master_window.geometry("300x300")
master_window.title("StringVar get() example")
 
def print_data():
    print(string_variable.get())
 
string_variable = tk.StringVar(master_window)
 
label = tk.Label(master_window, text="Enter Data: ")
label.grid(row=0, column=0)
 
entry = tk.Entry(master_window, textvariable=string_variable)
entry.grid(row=0, column=1)
 
button = tk.Button(master_window, text="Print data", command=print_data)
button.grid(row=1, column=0, columnspan=2)
 
master_window.mainloop()