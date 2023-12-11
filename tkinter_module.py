# tkinter_module.py

import tkinter as tk

def create_window(title, width, height):
    window = tk.Tk()
    window.title(title)
    window.geometry(f"{width}x{height}")
    return window

def create_label(window, text):
    label = tk.Label(window, text=text)
    return label

# You can add more functions for buttons, frames, etc.
