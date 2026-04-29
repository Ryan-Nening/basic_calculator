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

        def build_user_interface(self):
            title_font = font.Font(family="Helvetica", size=16, weight="bold")
            custom_font = font.Font(family="Helvetica", size=12)
            status_font = font.Font(family="Courier", size=10, slant="italic")

            self.title_label = tk.Label(self.main_window, text="⚡ NEON CALC PRO", font=title_font, bg="#0b0c10", fg="#66fcf1")
            self.title_label.pack(pady=(20, 10))

            self.status_label = tk.Label(self.main_window, text="Status: Waiting for inputs...", font=status_font, bg="#0b0c10", fg="#c5c6c7")
            self.status_label.pack(pady=(0, 10))    

    