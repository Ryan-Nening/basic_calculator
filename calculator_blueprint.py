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
        self.main_window.title("Basic Calculator")
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

        button_addition= tk.Button(self.button_frame, text="Add (+)", bg="#45a29e", fg="white", activebackground="#66fcf1", activeforeground="#0b0c10", width=10, relief="flat", cursor="hand2", command=lambda: self.evaluate("+"))
        button_addition.grid(row=0, column=0, padx=5, pady=5)
        self.addition_hover_animation(button_addition, "#66fcf1", "#0b0c10", "#45a29e", "white")

        button_subtraction = tk.Button(self.button_frame, text="Sub (-)", bg="#45a29e", fg="white", activebackground="#66fcf1", activeforeground="#0b0c10", width=10, relief="flat", cursor="hand2", command=lambda: self.evaluate("-"))
        button_subtraction.grid(row=0, column=1, padx=5, pady=5)
        self.addition_hover_animation(button_subtraction, "#66fcf1", "#0b0c10", "#45a29e", "white")

        button_multiplication = tk.Button(self.button_frame, text="Mult (*)", bg="#45a29e", fg="white", activebackground="#66fcf1", activeforeground="#0b0c10", width=10, relief="flat", cursor="hand2", command=lambda: self.evaluate("*"))
        button_multiplication.grid(row=1, column=0, padx=5, pady=5)
        self.add_hover_animation(button_multiplication, "#66fcf1", "#0b0c10", "#45a29e", "white")

        button_division = tk.Button(self.button_frame, text="Div (/)", bg="#45a29e", fg="white", activebackground="#66fcf1", activeforeground="#0b0c10", width=10, relief="flat", cursor="hand2", command=lambda: self.evaluate("/"))
        button_division.grid(row=1, column=1, padx=5, pady=5)
        self.addition_hover_animation(button_division, "#66fcf1", "#0b0c10", "#45a29e", "white")

        self.result_label = tk.Label(self.main_window, text="Result: --", font=title_font, bg="#0b0c10", fg="#45a29e")
        self.result_label.pack(pady=5)

        self.history_box = tk.Listbox(self.main_window, width=40, height=4, bg="#1f2833", fg="#c5c6c7", relief="flat", highlightthickness=0, font=("Courier", 10))
        self.history_box.pack(pady=5)

        self.control_frame = tk.Frame(self.main_window, bg="#0b0c10")
        self.control_frame.pack(pady=10)

        button_reset = tk.Button(self.control_frame, text="Try Again", bg="#2c3e50", fg="white", activebackground="#45a29e", activeforeground="white", width=12, relief="flat", cursor="hand2", command=self.reset_calculator)
        button_reset.grid(row=0, column=0, padx=5)
        self.addition_hover_animation(button_reset, "#45a29e", "white", "#2c3e50", "white")

        button_exit = tk.Button(self.control_frame, text="Exit", bg="#c0392b", fg="white", activebackground="#e74c3c", activeforeground="white", width=12, relief="flat", cursor="hand2", command=self.exit_program)
        button_exit.grid(row=0, column=1, padx=5)
        self.addition_hover_animation(button_exit, "#e74c3c", "white", "#c0392b", "white")

    def evaluate(self, operation):
        try:
            number1 = float(self.entry1.get())
            number2 = float(self.entry2.get())

            if operation == "+":
                result = self.add_numbers(number1, number2)
            elif operation == "-":
                result = self.subtract_numbers(number1, number2)
            elif operation == "*":
                result = self.multiply_numbers(number1, number2)
            elif operation == "/":
                result = self.divide_numbers(number1, number2)

            self.result_label.config(text=f"Result: {result}")
            self.status_label.config(text="Status: Calculation Success!", fg="#66fcf1") 
            self.history_box.insert(0, f"> {number1} {operation} {number2} = {result}")

        except ValueError:
            self.status_label.config(text="Status: Invalid Input Error!", fg="#ff4c4c") 
            messagebox.showerror("Input Error", "Please enter valid numeric values.")
        except ZeroDivisionError as e:
            self.status_label.config(text="Status: Math Error!", fg="#ff4c4c")
            messagebox.showerror("Math Error", str(e))
        except Exception:
            self.status_label.config(text="Status: Unknown Error!", fg="#ff4c4c")
            messagebox.showerror("Unknown Error", "Something went wrong.")

    def reset_calculator(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.result_label.config(text="Result: --")
        self.status_label.config(text="Status: Cleared. Waiting for inputs...", fg="#c5c6c7")
        self.entry1.focus()