import sympy as sp
import tkinter as tk
from tkinter import ttk, Button
from sympy import Eq, sympify, dsolve
#values of x and y
x, C_1, C_2 = sp.symbols("x C_1 C_2")
y = sp.Function('y')(x)

#replacing symbols
def replacement(problem):
    replacements = {
        ' ': '',
        'e^': 'exp',
        '^': '**',
        '{': '(',
        '}': ')'
    }   
    for find, replace in replacements.items():
        problem = problem.replace(find, replace)
    return problem

#caluclating separable values
def calculate_separable():
    problem = entry_equation.get()
    problem = problem.lower() #sympify doesn't work on capital letter, therefore we use small letters
    problem = problem.replace(' ','') # Remove space
    problem = problem.replace("dy/dx", "Derivative(y,x)")
    eqlhs, eqrhs = problem.split('=')
    problem = replacement(problem)
    problem = problem.replace("y", "y(x)")
    print(problem)
    # Initialize variables to store left-hand side and right-hand side of equations
    eqlhs, eqrhs = problem.split('=')
    # display the user-provided equations
    eqlhs = sympify(eqlhs)   
    eqrhs = sympify(eqrhs)
    equation = Eq(eqlhs, eqrhs)
    result_text = f"\n<Result>\n"
    result_text += f"\nEquation :\n{sp.pretty(equation)}\n"
    # Solve the seperable variable using dsolve()
    solution = dsolve(equation)
    result_text += f"\nFinal answer:\n{sp.pretty(solution)}"
    print(result_text)
    result_label.insert(tk.END, result_text)
    

        
# Create the main window
root = tk.Tk()
root.title("Separable Variables Calculator")
root.geometry("500x400")
# Labels and textboxs
label_equation = tk.Label(root, text="Enter your differential equation:")
label_equation.pack(pady=5)

entry_equation = ttk.Entry(root, width=50)
entry_equation.pack(pady=10)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_separable)
calculate_button.pack(pady=10)

frame = ttk.Frame(root, style='My.TFrame')
frame.pack( pady=10, fill=tk.BOTH, expand=True)
#for rest buttons
def clear():
    entry_equation.delete(0, tk.END)
    result_label.delete(1.0, tk.END)

reset_button = ttk.Button(root, text="Reset", command=clear)
reset_button.pack(pady=10)

# big Text box for answer disp.
result_label = tk.Text(root, bg="#add8e6", wrap=tk.WORD, width=50, height=10)
result_label.place(relx=0.5, rely=0.5, anchor='center', y=10)

# Run the Tkinter main loop
root.mainloop()
