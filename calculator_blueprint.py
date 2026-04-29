import tkinter as tk
from tkinter import messagebox, font

class BaseCalculator:
    def add_numbers(self, a, b):
        return a + b

    def subtract_numbers(self, a, b):
        return a - b

    def multiply_numbers(self, a, b):
        return a * b

    def divide_numbers(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b

    class GuiCalculator(BaseCalculator):
        def __init__(self):
            self.main_window = tk.Tk()
            self.main_window.title("App Calculator Pro")
            self.main_window.geometry("400x560")
            self.main_window.configure(bg="#0b0c10")

        def add_hover_animation(self, widget, hover_bg, hover_fg, normal_bg, normal_fg):
            widget.bind("<Enter>", lambda e: widget.config(bg=hover_bg, fg=hover_fg))
            widget.bind("<Leave>", lambda e: widget.config(bg=normal_bg, fg=normal_fg))

    