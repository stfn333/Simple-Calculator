import tkinter as tk


class Calculator:
    """
    A simple calculator application using Tkinter.
    """

    def __init__(self):
        """
        Initializes the calculator GUI.
        """
        self.root = tk.Tk()
        self.root.title("Simple Calculator")

        # Entry widget for displaying and entering numbers
        self.entry = tk.Entry(self.root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Variables to store previous number and current math operation
        self.previous_number = None
        self.math_operation = ""

        # Create number buttons and operator buttons
        self.create_number_buttons()
        self.create_operator_buttons()

    def create_number_buttons(self):
        """
        Creates number buttons (0-9) and binds them to the insert_digit method.
        """
        for i in range(10):
            button = tk.Button(text=i, padx=40, pady=20,
                               command=lambda num=i: self.insert_digit(num))
            button.grid(row=(i // 3) + 1, column=i % 3)

    def insert_digit(self, number):
        """
        Inserts the given digit into the entry widget.
        """
        current_digit = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, f"{current_digit}{number}")

    def create_operator_buttons(self):
        """
        Creates operator buttons (+, -, *, /, =, C) and binds them to corresponding methods.
        """
        # Addition button
        add = tk.Button(self.root, text="+", padx=40, pady=20, command=self.add)
        add.grid(row=4, column=1)

        # Subtraction button
        subtract = tk.Button(self.root, text="-", padx=40, pady=20, command=self.subtract)
        subtract.grid(row=4, column=2)

        # Multiplication button
        multiply = tk.Button(self.root, text="X", padx=40, pady=20, command=self.multiply)
        multiply.grid(row=5, column=0)

        # Division button
        divide = tk.Button(self.root, text="/", padx=40, pady=20, command=self.divide)
        divide.grid(row=5, column=1)

        # Equals button
        equals = tk.Button(self.root, text="=", padx=135, pady=20, command=self.equals)
        equals.grid(row=6, column=0, columnspan=3)

        # Clear button
        clear = tk.Button(self.root, text="C", padx=40, pady=20, command=self.clear)
        clear.grid(row=5, column=2)

    def clear(self):
        """
        Clears the entry widget.
        """
        self.entry.delete(0, tk.END)

    def add(self):
        """
        Sets the math_operation to addition and stores the previous number.
        """
        self.previous_number = int(self.entry.get())
        self.math_operation = "addition"
        self.entry.delete(0, tk.END)

    def subtract(self):
        """
        Sets the math_operation to subtraction and stores the previous number.
        """
        self.previous_number = int(self.entry.get())
        self.math_operation = "subtraction"
        self.entry.delete(0, tk.END)

    def multiply(self):
        """
        Sets the math_operation to multiplication and stores the previous number.
        """
        self.previous_number = int(self.entry.get())
        self.math_operation = "multiplication"
        self.entry.delete(0, tk.END)

    def divide(self):
        """
        Sets the math_operation to division and stores the previous number.
        """
        self.previous_number = int(self.entry.get())
        self.math_operation = "division"
        self.entry.delete(0, tk.END)

    def equals(self):
        """
        Performs the arithmetic operation based on the selected math_operation.
        """
        current_number = int(self.entry.get())
        self.entry.delete(0, tk.END)

        if self.math_operation == "addition":
            result = self.previous_number + current_number
        elif self.math_operation == "subtraction":
            result = self.previous_number - current_number
        elif self.math_operation == "multiplication":
            result = self.previous_number * current_number
        elif self.math_operation == "division":
            if current_number == 0:
                result = "Invalid operation!"
            else:
                result = self.previous_number / current_number

        self.entry.insert(0, result)

    def run(self):
        """
        Starts the Tkinter event loop.
        """
        self.root.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
