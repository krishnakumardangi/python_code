# Owner: Krishna Kumar
# File Name: tk_in_matplaotlib.py
# Description: Implementation of matplotlib in tk
# Date: 14-12-2023
# Status: Ok
'''
This code creates a simple Tkinter window with a label, an entry widget for frequency input, and a button to update the plot. The Matplotlib plot is embedded in the Tkinter window using FigureCanvasTkAgg. The update_plot function is called when the button is pressed, and it updates the Matplotlib plot based on the entered frequency.
'''
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_plot():
    # Get the frequency value from the entry widget
    #print(frequency_entry.get())
    f =frequency_entry.get()
    if f=='':
        frequency = 10
    else:
        frequency = float(frequency_entry.get())
    
    # Generate x values
    x = np.linspace(0, 2 * np.pi, 1000)

    # Calculate y values for the sine function with the specified frequency
    y = np.sin(frequency * x)

    # Clear the previous plot
    ax.clear()

    # Plot the new sine function
    ax.plot(x, y, label=f'Sine Function (Frequency = {frequency})')
    ax.legend()

    # Update the canvas
    canvas.draw()

# Create the main Tkinter window
root = tk.Tk()
root.title("Matplotlib with Tkinter")

# Create a Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(5, 4), tight_layout=True)

# Create a Tkinter canvas that can be embedded in the GUI
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a label and entry for the frequency input
frequency_label = ttk.Label(root, text="Frequency:")
frequency_label.pack(side=tk.LEFT, padx=10)
frequency_entry = ttk.Entry(root)
frequency_entry.pack(side=tk.LEFT, padx=10)

# Create a button to update the plot
update_button = ttk.Button(root, text="Update Plot", command=update_plot)
update_button.pack(side=tk.LEFT, padx=10)

# Initial plot
update_plot()

#to show exit button and exit from game
exit_the_game= ttk.Button(root, text="Exit Game", command=root.quit)
exit_the_game.pack(side = tk.LEFT, padx = 10)

# Start the Tkinter event loop
root.mainloop()
