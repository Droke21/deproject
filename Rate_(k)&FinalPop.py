import tkinter as tk
from tkinter import ttk, Label, Entry, Button, Toplevel
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

pastel_blue = "#add8e6"  #83978

active_entry = None
rate_result_label1 = None
def set_active_entry(entry):
    global active_entry
    active_entry = entry

#final pop
def population_formula(P0, k, t):
    return P0 * np.exp(k * t)

# calculations
def calculate_population():
    global rate_result_label1
    try:
        P0 = float(initial_entry.get())
        k = float(rate_entry.get())
        t = float(time_entry.get())

        t_values = np.linspace(0, t, 400)
        P_values = population_formula(P0, k, t_values)

        result_label.config(text=f"Population at time {t}: {P_values[-1]:.2f} is the Final Population")#disp result

        # Create and display the graph
        plt.style.use("dark_background")
        fig, ax = plt.subplots()
        ax.plot(t_values, P_values)
        ax.set_xlabel('Time')
        ax.set_ylabel('Population')
        ax.set_title('Growth/Decay Equation Solution Graph')

        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, pady=10)

        if rate_result_label1:
            rate_result_label1.config(text=f"Initial Population (P0): {P0:.2f}\n"
                                          f"at Time (t): {t:.2f}\n"
                                          f"Rate of change (k): {k:.6f}\n"
                                          f"\nFinal Population: {P_values[-1]:.2f}",wraplength=400)
        else:
            rate_result_label1 = Label(root, text="", font=('Verdana', 16), bg=pastel_blue)
            rate_result_label1.pack(pady=10, padx=250, anchor=tk.SE)
            rate_result_label1.config(text=f"Initial Population (P0): {P0:.2f}\nat Time (t): {t:.2f}\nRate of change (k): {k:.6f}\n\nFinal Population: {P_values[-1]:.2f}", wraplength=400)

    except ValueError:
        result_label.config(text="Please enter valid numbers for the parameters.")
#calculation for k
def calculate_rate_of_change():
    try:
        P0 = float(initial_rate_entry.get())
        P1= float(final_rate_entry.get())
        t = float(time_rate_entry.get())

        k = np.log(P1 / P0) / t
        
        rate_result_label.config(text=f"Initial Population (P0): {P0:.2f}\nFinal Population (P): {P1:.2f}\nTime (t): {t:.2f}\n\nRate of change (k): {k:.6f}")#disp result

    except ValueError:
        rate_result_label.config(text="Please enter valid numbers for the parameters.")
        
def reset_values():
    # Reset button
    global rate_result_label1
    
    initial_entry.delete(0, tk.END)
    initial_entry.insert(0, "0")

    rate_entry.delete(0, tk.END)
    rate_entry.insert(0, "0")

    time_entry.delete(0, tk.END)
    time_entry.insert(0, "0")

    initial_rate_entry.delete(0, tk.END)
    initial_rate_entry.insert(0, "0")

    final_rate_entry.delete(0, tk.END)
    final_rate_entry.insert(0, "0")

    time_rate_entry.delete(0, tk.END)
    time_rate_entry.insert(0, "0")

    # Reset result
     # Reset rate_result_label1
    rate_result_label1.config(text="")
    result_label.config(text="")
    rate_result_label.config(text="")

    #GRAPH RESETS
    for widget in graph_frame.winfo_children():
        widget.destroy()

#bgcolor
root = tk.Tk()
root.title("Rate(K) and Final Population Calculator")
root.configure(bg=pastel_blue)

style = ttk.Style()
style.configure('My.TFrame', background=pastel_blue)

frame = ttk.Frame(root, style='My.TFrame')
frame.pack(side=tk.LEFT, padx=50, pady=30, fill=tk.BOTH, expand=True)
#screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Calculate Population GUI
rate_label = Label(frame, text="Rate (k):", font=('Verdana', 16), bg=pastel_blue)
rate_label.grid(row=0, column=0, pady=5)
rate_entry = Entry(frame, font=('Verdana', 16))
rate_entry.grid(row=0, column=1, pady=5)
rate_entry.bind("<FocusIn>", lambda event: set_active_entry(rate_entry))

initial_label = Label(frame, text="Initial Population (P0):", font=('Verdana', 16), bg=pastel_blue)
initial_label.grid(row=1, column=0, pady=5)
initial_entry = Entry(frame, font=('Verdana', 16))
initial_entry.grid(row=1, column=1, pady=5)
initial_entry.bind("<FocusIn>", lambda event: set_active_entry(initial_entry))

time_label = Label(frame, text="Time (t):", font=('Verdana', 16), bg=pastel_blue)
time_label.grid(row=2, column=0, pady=5)
time_entry = Entry(frame, font=('Verdana', 16))
time_entry.grid(row=2, column=1, pady=5)
time_entry.bind("<FocusIn>", lambda event: set_active_entry(time_entry))

result_label = Label(frame, text="", font=('Verdana', 16), bg=pastel_blue)
result_label.grid(row=3, columnspan=2, pady=10)

# Graph frame
graph_frame = ttk.Frame(root, style='My.TFrame')
graph_frame.pack(pady=20, padx=80, side=tk.TOP, anchor=tk.NE) 

# Solve and Reset buttons
solve_population = Button(frame, text="Solve for Population", font=('Verdana', 16), command=calculate_population)
solve_population.grid(row=4, columnspan=2, pady=10)

reset_button = Button(frame, text="Reset", font=('Verdana', 16), command=reset_values)
reset_button.grid(row=6, columnspan=2, pady=10)


#Calculate rate of change GUI or k
initial_rate_label = Label(frame, text="Initial Population (P0):", font=('Verdana', 16), bg=pastel_blue)
initial_rate_label.grid(row=7, column=0, pady=5)
initial_rate_entry = Entry(frame, font=('Verdana', 16))
initial_rate_entry.grid(row=7, column=1, pady=5)
initial_rate_entry.bind("<FocusIn>", lambda event: set_active_entry(initial_rate_entry))

final_rate_label = Label(frame, text="(P1):", font=('Verdana', 16), bg=pastel_blue)
final_rate_label.grid(row=8, column=0, pady=5)
final_rate_entry = Entry(frame, font=('Verdana', 16))
final_rate_entry.grid(row=8, column=1, pady=5)
final_rate_entry.bind("<FocusIn>", lambda event: set_active_entry(final_rate_entry))

time_rate_label = Label(frame, text="Time (t1):", font=('Verdana', 16), bg=pastel_blue)
time_rate_label.grid(row=9, column=0, pady=5)
time_rate_entry = Entry(frame, font=('Verdana', 16))
time_rate_entry.grid(row=9, column=1, pady=5)
time_rate_entry.bind("<FocusIn>", lambda event: set_active_entry(time_rate_entry))

#CALCULATE K BUTTON
calculate_rate_button = Button(frame, text="Calculate for k", font=('Verdana', 16), command=calculate_rate_of_change)
calculate_rate_button.grid(row=10, columnspan=2, pady=10)

rate_result_label = Label(frame, text="", font=('Verdana', 16), bg=pastel_blue)
rate_result_label.grid(row=11, columnspan=2, pady=10)

root.mainloop()
