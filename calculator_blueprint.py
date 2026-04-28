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