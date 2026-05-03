# BASIC CALCULATOR

**A Cyberpunk-Themed Object-Oriented Calculator**  

## Program Overview
This project is a Simple App Calculator built using Python and the Tkinter GUI library. It was developed to demonstrate fundamental Object-Oriented Programming (OOP) concepts such as **Inheritance** and proper **Exception Handling** during runtime. 

Instead of a standard terminal output, this calculator features a custom "Cyberpunk Neon" graphical interface with interactive animations, a dynamic status bar, and a live history log.

## Features
* **Standard Math Operations:** Performs addition, subtraction, multiplication, and division.
* **OOP Architecture:** Uses a Parent-Child class structure (`BaseCalculator` and `GuiCalculator`) to separate the math logic from the interface.
* **Runtime Exception Handling:** Safely catches `ValueError` (if a user types letters) and `ZeroDivisionError` using `try-except` blocks, preventing the program from crashing.
* **Interactive UI:** Features mouse hover glow effects, active click states, and highlighted text box borders.
* **Dynamic Status Bar:** Provides real-time feedback (Cyan for success, Red for errors).
* **Digital Receipt Log:** Automatically saves all successful computations into a live history board.
* **Program Controls:** Includes a "Try Again" loop to reset the board and an "Exit" button that displays a farewell message before closing safely.

## How to Run the Program

**Prerequisites:** 
You need to have Python installed on your computer. The `tkinter` and `messagebox` libraries are built into Python, so no extra installations are required.

**Steps:**
1. Clone or download this repository to your local machine.
2. Open the project folder in your preferred IDE (like VS Code) or terminal.
3. Run the main execution file:
```bash
python main_calculator.py
