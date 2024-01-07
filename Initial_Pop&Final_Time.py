import tkinter as tk
from tkinter import ttk, Label, Entry, Button
import numpy as np

pastel_blue = "#add8e6"

active_entry = None
result_text_growth_decay = None
result_text_initial_pop = None

def set_active_entry(entry):
    global active_entry
    active_entry = entry

def calculate_time(ini_entry, t1_entry, p1_entry, pf_entry, output_text):
    try:
        P0 = float(ini_entry.get())
        t1 = float(t1_entry.get())
        P1 = float(p1_entry.get())
        P3 = float(pf_entry.get())

        k = np.log(P1 / P0) / t1
        final_time = np.log(P3 / P0) / k

        result_text_growth_decay.config(text=f"Final time (t3): {final_time:.2f}")
        output_text.config(text="")  # Clear previous error message

    except ValueError:
        result_text_growth_decay.config(text="")
        output_text.config(text="Please enter valid numbers for the parameters.")

def calculate_initialpop(t1_entry, p1_entry, t3_entry, p3_entry, output_text):
    try:
        t1 = float(t1_entry.get())
        P1 = float(p1_entry.get())
        t3 = float(t3_entry.get())
        P3 = float(p3_entry.get())

        k = np.log(P1 / P3) / (t1 - t3)
        P0 = P1 / np.exp(k * t1)

        result_text_initial_pop.config(text=f"Initial Population (P0): {P0:.2f}")
        output_text.config(text="")  # Clear previous error message

    except ValueError:
        result_text_initial_pop.config(text="")
        output_text.config(text="Please enter valid numbers for the parameters.")

def reset_fields(initial_entry, t1_entry, p1_entry, pf_entry, result_text, output_text):
    initial_entry.delete(0, tk.END)
    t1_entry.delete(0, tk.END)
    p1_entry.delete(0, tk.END)
    pf_entry.delete(0, tk.END)
    result_text.config(text="")
    output_text.config(text="")

def reset_fields_initial_pop(t1_entry, p1_entry, t3_entry, p3_entry, result_text, output_text):
    t1_entry.delete(0, tk.END)
    p1_entry.delete(0, tk.END)
    t3_entry.delete(0, tk.END)
    p3_entry.delete(0, tk.END)
    result_text.config(text="")
    output_text.config(text="")

root = tk.Tk()
root.title("Final Time and Initial Population Calculator")
root.configure(bg=pastel_blue)

style = ttk.Style()
style.configure('My.TFrame', background=pastel_blue)

frame = ttk.Frame(root, style='My.TFrame')
frame.pack(side=tk.LEFT, padx=50, pady=30, fill=tk.BOTH, expand=True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Growth/Decay Calculator Section
entry_label_growth_decay = Label(frame, text="Initial Population (P0): ", font=('Verdana', 16), bg=pastel_blue)
entry_label_growth_decay.grid(row=13, column=0, pady=5)
initial_entry2_growth_decay = Entry(frame, font=('Verdana', 16))
initial_entry2_growth_decay.grid(row=13, column=1, pady=5)
initial_entry2_growth_decay.bind("<FocusIn>", lambda event: set_active_entry(initial_entry2_growth_decay))

entry_label_p1_growth_decay = Label(frame, text="P1: ", font=('Verdana', 16), bg=pastel_blue)
entry_label_p1_growth_decay.grid(row=14, column=0, pady=5)
p1_entry_growth_decay = Entry(frame, font=('Verdana', 16))
p1_entry_growth_decay.grid(row=14, column=1, pady=5)
p1_entry_growth_decay.bind("<FocusIn>", lambda event: set_active_entry(p1_entry_growth_decay))

entry_label_t1_growth_decay = Label(frame, text="t1: ", font=('Verdana', 16), bg=pastel_blue)
entry_label_t1_growth_decay.grid(row=15, column=0, pady=5)
t1_entry_growth_decay = Entry(frame, font=('Verdana', 16))
t1_entry_growth_decay.grid(row=15, column=1, pady=5)
t1_entry_growth_decay.bind("<FocusIn>", lambda event: set_active_entry(t1_entry_growth_decay))

entry_label_p3_growth_decay = Label(frame, text="Final Population: ", font=('Verdana', 16), bg=pastel_blue)
entry_label_p3_growth_decay.grid(row=16, column=0, pady=5)
pf_entry_growth_decay = Entry(frame, font=('Verdana', 16))
pf_entry_growth_decay.grid(row=16, column=1, pady=5)
pf_entry_growth_decay.bind("<FocusIn>", lambda event: set_active_entry(pf_entry_growth_decay))

output_label_growth_decay = Label(root, text="", font=('Verdana', 16))
output_label_growth_decay.pack(pady=10)

result_text_growth_decay = Label(frame, text="", font=('Verdana', 16), bg=pastel_blue)
result_text_growth_decay.grid(row=17, columnspan=2, pady=10)

solve_button_growth_decay = Button(frame, text="Calculate for Final Time", font=('Verdana', 16), command=lambda: calculate_time(initial_entry2_growth_decay, t1_entry_growth_decay, p1_entry_growth_decay, pf_entry_growth_decay, output_label_growth_decay))
solve_button_growth_decay.grid(row=18, columnspan=2, pady=10)

reset_button_growth_decay = Button(frame, text="Reset", font=('Verdana', 16), command=lambda: reset_fields(initial_entry2_growth_decay, t1_entry_growth_decay, p1_entry_growth_decay, pf_entry_growth_decay, result_text_growth_decay, output_label_growth_decay))
reset_button_growth_decay.grid(row=19, columnspan=2, pady=10)

# Initial Population Calculator Section
t1_label_initial_pop = Label(frame, text="t1: ", font=('Verdana', 16), bg=pastel_blue)
t1_label_initial_pop.grid(row=20, column=0, pady=5)
t1_entry_initial_pop = Entry(frame, font=('Verdana', 16))
t1_entry_initial_pop.grid(row=20, column=1, pady=5)
t1_entry_initial_pop.bind("<FocusIn>", lambda event: set_active_entry(t1_entry_initial_pop))

p1_label_initial_pop = Label(frame, text="P1: ", font=('Verdana', 16), bg=pastel_blue)
p1_label_initial_pop.grid(row=21, column=0, pady=5)
p1_entry_initial_pop = Entry(frame, font=('Verdana', 16))
p1_entry_initial_pop.grid(row=21, column=1, pady=5)
p1_entry_initial_pop.bind("<FocusIn>", lambda event: set_active_entry(p1_entry_initial_pop))

t3_label_initial_pop = Label(frame, text="t3: ", font=('Verdana', 16), bg=pastel_blue)
t3_label_initial_pop.grid(row=22, column=0, pady=5)
t3_entry_initial_pop = Entry(frame, font=('Verdana', 16))
t3_entry_initial_pop.grid(row=22, column=1, pady=5)
t3_entry_initial_pop.bind("<FocusIn>", lambda event: set_active_entry(t3_entry_initial_pop))

p3_label_initial_pop = Label(frame, text="Final Population: ", font=('Verdana', 16), bg=pastel_blue)
p3_label_initial_pop.grid(row=23, column=0, pady=5)
p3_entry_initial_pop = Entry(frame, font=('Verdana', 16))
p3_entry_initial_pop.grid(row=23, column=1, pady=5)
p3_entry_initial_pop.bind("<FocusIn>", lambda event: set_active_entry(p3_entry_initial_pop))

output_label_initial_pop = Label(root, text="", font=('Verdana', 16))
output_label_initial_pop.pack(pady=10)

result_text_initial_pop = Label(frame, text="", font=('Verdana', 16), bg=pastel_blue)
result_text_initial_pop.grid(row=24, columnspan=2, pady=10)

solve_button_initial_pop = Button(frame, text="Calculate Initial Population", font=('Verdana', 16), command=lambda: calculate_initialpop(t1_entry_initial_pop, p1_entry_initial_pop, t3_entry_initial_pop, p3_entry_initial_pop, output_label_initial_pop))
solve_button_initial_pop.grid(row=25, columnspan=2, pady=10)

reset_button_initial_pop = Button(frame, text="Reset", font=('Verdana', 16), command=lambda: reset_fields_initial_pop(t1_entry_initial_pop, p1_entry_initial_pop, t3_entry_initial_pop, p3_entry_initial_pop, result_text_initial_pop, output_label_initial_pop))
reset_button_initial_pop.grid(row=26, columnspan=2, pady=10)

root.mainloop()
