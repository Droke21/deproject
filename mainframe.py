import tkinter as tk
from subprocess import Popen

def open_project(project_command):
    Popen(["python", project_command])

def create_main_gui():
    root = tk.Tk()
    root.title("Main GUI")
    root.geometry("600x400")  # Set the size of the main window
    root.configure(bg="#ADD8E6")

    # Function to open Project 1
    def open_project1():
        open_project("desep.py")

    # Function to open Project 2
    def open_project2():
        open_project("Rate_(k)&FinalPop.py")

    # Function to open Project 3
    def open_project3():
        open_project("Initial_Pop&Final_Time.py")

    # Buttons to open each project with a larger font size
    button1 = tk.Button(root, text="Separable Variables Calculator", command=open_project1, font=("Helvetica", 12))
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Growth and Decay Calculator (Rate(K) and Final Population)", command=open_project2, font=("Helvetica", 12))
    button2.pack(pady=10)

    button3 = tk.Button(root, text="Growth and Decay Calculator (Initial Poulation and Final Time)", command=open_project3, font=("Helvetica", 12))
    button3.pack(pady=10)

    root.mainloop()

# Call the function to create the main GUI
create_main_gui()
