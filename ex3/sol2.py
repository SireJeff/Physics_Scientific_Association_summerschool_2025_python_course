# solution_q2.py

import tkinter as tk
from tkinter import ttk
import numpy as np

class QuadraticSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quadratic Solver")
        self.root.geometry("400x200")

        # --- Create and layout widgets ---
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Coefficient inputs
        ttk.Label(main_frame, text="ax² + bx + c = 0").grid(row=0, column=0, columnspan=3, pady=10)
        
        self.a_var = tk.StringVar()
        self.b_var = tk.StringVar()
        self.c_var = tk.StringVar()

        ttk.Entry(main_frame, textvariable=self.a_var, width=5).grid(row=1, column=0, padx=5)
        ttk.Label(main_frame, text="x² +").grid(row=1, column=1)
        ttk.Entry(main_frame, textvariable=self.b_var, width=5).grid(row=1, column=2, padx=5)
        ttk.Label(main_frame, text="x +").grid(row=1, column=3)
        ttk.Entry(main_frame, textvariable=self.c_var, width=5).grid(row=1, column=4, padx=5)
        ttk.Label(main_frame, text="= 0").grid(row=1, column=5)

        # Calculate button
        calc_button = ttk.Button(main_frame, text="Calculate Roots", command=self.calculate_roots)
        calc_button.grid(row=2, column=0, columnspan=6, pady=20)
        
        # Result display
        self.result_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.result_var, font=("Helvetica", 12)).grid(row=3, column=0, columnspan=6)

    def calculate_roots(self):
        """Callback function to calculate and display the roots."""
        try:
            # Get values and convert to float
            a = float(self.a_var.get())
            b = float(self.b_var.get())
            c = float(self.c_var.get())
            
            if a == 0:
                self.result_var.set("Error: 'a' cannot be zero.")
                return

            # Use numpy.roots to find the roots
            coefficients = [a, b, c]
            roots = np.roots(coefficients)
            
            # Format the result string
            if len(roots) == 1:
                result_str = f"Double Root: {roots[0]:.4f}"
            else:
                root1_str = f"{roots[0]:.4f}" if np.isreal(roots[0]) else f"{roots[0]:.4f}"
                root2_str = f"{roots[1]:.4f}" if np.isreal(roots[1]) else f"{roots[1]:.4f}"
                result_str = f"Roots: {root1_str}, {root2_str}"

            self.result_var.set(result_str)

        except ValueError:
            self.result_var.set("Error: Please enter valid numbers.")
        except Exception as e:
            self.result_var.set(f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuadraticSolverApp(root)
    root.mainloop()