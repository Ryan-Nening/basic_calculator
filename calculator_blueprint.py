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

            self.instruction1 = tk.Label(self.main_window, text="Enter First Number:", font=custom_font, bg="#0b0c10", fg="#ffffff")
            self.instruction1.pack()
            self.entry1 = tk.Entry(self.main_window, font=custom_font, justify="center", bg="#1f2833", fg="#66fcf1", insertbackground="white", relief="solid", highlightthickness=2, highlightcolor="#66fcf1", highlightbackground="#0b0c10")
            self.entry1.pack(pady=5, ipady=5)

            self.instruction2 = tk.Label(self.main_window, text="Enter Second Number:", font=custom_font, bg="#0b0c10", fg="#ffffff")
            self.instruction2.pack()
            self.entry2 = tk.Entry(self.main_window, font=custom_font, justify="center", bg="#1f2833", fg="#66fcf1", insertbackground="white", relief="solid", highlightthickness=2, highlightcolor="#66fcf1", highlightbackground="#0b0c10")
            self.entry2.pack(pady=5, ipady=5)

            self.button_frame = tk.Frame(self.main_window, bg="#0b0c10")
            self.button_frame.pack(pady=15)

            btn_add = tk.Button(self.button_frame, text="Add (+)", bg="#45a29e", fg="white", activebackground="#66fcf1", activeforeground="#0b0c10", width=10, relief="flat", cursor="hand2", command=lambda: self.evaluate("+"))
            btn_add.grid(row=0, column=0, padx=5, pady=5)
            self.add_hover_animation(btn_add, "#66fcf1", "#0b0c10", "#45a29e", "white")

            btn_sub = tk.Button(self.button_frame, text="Sub (-)", bg="#45a29e", fg="white", activebackground="#66fcf1", activeforeground="#0b0c10", width=10, relief="flat", cursor="hand2", command=lambda: self.evaluate("-"))
            btn_sub.grid(row=0, column=1, padx=5, pady=5)
            self.add_hover_animation(btn_sub, "#66fcf1", "#0b0c10", "#45a29e", "white")

            btn_mult = tk.Button(self.button_frame, text="Mult (*)", bg="#45a29e", fg="white", activebackground="#66fcf1", activeforeground="#0b0c10", width=10, relief="flat", cursor="hand2", command=lambda: self.evaluate("*"))
            btn_mult.grid(row=1, column=0, padx=5, pady=5)
            self.add_hover_animation(btn_mult, "#66fcf1", "#0b0c10", "#45a29e", "white")

            btn_div = tk.Button(self.button_frame, text="Div (/)", bg="#45a29e", fg="white", activebackground="#66fcf1", activeforeground="#0b0c10", width=10, relief="flat", cursor="hand2", command=lambda: self.evaluate("/"))
            btn_div.grid(row=1, column=1, padx=5, pady=5)
            self.add_hover_animation(btn_div, "#66fcf1", "#0b0c10", "#45a29e", "white")

        