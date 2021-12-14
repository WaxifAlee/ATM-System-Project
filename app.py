import tkinter as tk
from tkinter import Message, ttk
from tkinter import Frame, filedialog
import time as t
import os

# Basic Credentials on the console
"""os.system("cls")
print("+----------------  H E L L O  T H E R E  !! -----------------+\n")
t.sleep(0.2)
print("+--- This ATM System Was Created By Wasif Ali & Marium Ilyas ---+\n")
input('Press Any Key To Continue...')"""


# Creating the main GUI Structure i.e. Root of the program
root = tk.Tk()
root.resizable(False, False)
root.title("ATM System")
#root.geometry("768x480")
# Giving a background canvas to the app

canvas = tk.Canvas(root, height=400, width=400, bg="#B8E4F0")
canvas.pack()

frame = Frame(root, bg="#98BAE7")
frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)

label = tk.Label(frame, text="Login To The ATM System", padx=10, pady=40, font=("Poppins, 18"), bg="#98bae7")
label.pack()


root.mainloop()