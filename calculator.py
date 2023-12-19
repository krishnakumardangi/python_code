import tkinter as tk
from math import *

def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(value))

def clear_entry():
    entry_var.set("")

def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

def calculate_square_root():
    try:
        result = sqrt(float(entry_var.get()))
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

def calculate_square():
    try:
        result = pow(float(entry_var.get()), 2)
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

def calculate_inverse():
    try:
        result = 1 / float(entry_var.get())
        entry_var.set(result)
    except ZeroDivisionError:
        entry_var.set("Error: Division by zero")
    except Exception as e:
        entry_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Advanced Calculator")

# Entry widget for displaying the input and result
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=6, sticky="nsew")

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'sin', 'cos', 'tan', '^2',
    'sqrt', '(', ')', '1/x',
    'C'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 12), command=calculate_result).grid(row=row_val, column=col_val)
    elif button == 'sin':
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 12), command=lambda: on_button_click("sin(")).grid(row=row_val, column=col_val)
    elif button == 'cos':
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 12), command=lambda: on_button_click("cos(")).grid(row=row_val, column=col_val)
    elif button == 'tan':
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 12), command=lambda: on_button_click("tan(")).grid(row=row_val, column=col_val)
    elif button == '^2':
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 12), command=calculate_square).grid(row=row_val, column=col_val)
    elif button == 'sqrt':
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 12), command=calculate_square_root).grid(row=row_val, column=col_val)
    elif button == '1/x':
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 12), command=calculate_inverse).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 12), command=clear_entry).grid(row=row_val, column=col_val, columnspan=2)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 12), command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 5:
        col_val = 0
        row_val += 1

# Configure row and column weights
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the GUI
root.mainloop()
