🧮 Python Tkinter Calculator

A sleek desktop calculator built with Python’s Tkinter GUI toolkit — simple, functional, and styled with a modern dark theme. This project demonstrates dynamic widget creation, event handling, and basic expression evaluation, making it ideal for Python beginners and GUI enthusiasts.

🔍 Overview

This calculator supports:

Basic arithmetic operations (+, -, *, /)

Floating point numbers

Clear (C) and Backspace (⌫)

Real-time evaluation using eval() with safe UI behavior

It’s designed to mimic a physical calculator’s layout and feel, while being visually clean and intuitive.

🛠️ Features

✔️ Dynamic button generation
✔️ Responsive Entry display
✔️ Clear and backspace functions
✔️ Dark theme for modern look
✔️ Error handling for invalid inputs

🚀 Why This Project?
This is more than a calculator — it’s a learning tool that illustrates:
Python function bindings
Lambda usage to avoid loop late-binding pitfalls
GUI layout with grid()
Handling user interaction in desktop apps
Perfect for students and hobbyists exploring GUI development.

📦 Installation

1.Clone the repository:
git clone https://github.com/<your-username>/tkinter-calculator.git
cd tkinter-calculator

2.Run the application
python calculator.py
💡 Works with Python 3.x — Tkinter is included by default.

🧠 How It Works

Each button press calls press(v) which adds the character to the entry.
calc() evaluates the string expression using eval() and updates the screen.
clear() wipes the display, and backspace() removes the last character.
Operators are styled differently for usability.
