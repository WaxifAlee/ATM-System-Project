import tkinter as tk
from tkinter import Canvas, Message, ttk
from tkinter import Frame, filedialog
import time as t
import os

# Basic Credentials on the console
"""os.system("cls")
print("+----------------  H E L L O  T H E R E  !! -----------------+\n")
t.sleep(0.2)
print("+--- This ATM System Was Created By Wasif Ali & Marium Ilyas ---+\n")
input('Press Any Key To Continue...')"""

# Defining the functions for creating new windows


def credits_window(dev1, dev2):
    credits_window = tk.Toplevel(root)
    credits_window.wm_geometry("400x200")
    credits_window.resizable(False, False)
    plate = Canvas(credits_window, height=300, width=300)
    label1 = tk.Label(plate, text="Developers Of The Project:", font=("Arial, 16"))
    label1.pack(pady=10)

    names_lbl = tk.Label(plate, text=f"Presented By:\n\n1. {dev1}\n       2. {dev2}")
    names_lbl.pack(pady=10)
    teach_lbl = tk.Label(plate, text=f"Submitted To: Miss Beenish Noor")
    teach_lbl.pack(pady=5)

    plate.pack()


# Creating the main GUI Structure i.e. Root of the program
root = tk.Tk()
root.resizable(False, False)
root.title("ATM System")
# Giving a background canvas to the app

canvas = tk.Canvas(root, height=400, width=400, bg="#B8E4F0")
canvas.pack()

frame = Frame(root, bg="#98BAE7")
frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)

label = tk.Label(
    frame,
    text="Login To The ATM System",
    padx=10,
    pady=40,
    font=("sans-serif, 18"),
    bg="#98bae7",
)
label.pack()

btn_login = tk.Button(frame, text="Login", padx=40, pady=10).pack(pady=10)
btn_credits = tk.Button(
    frame,
    text="About Developers",
    padx=8,
    pady=10,
    command=lambda: credits_window(
        "Wasif Ali [FA21-BCS-035]", "Marium Ilyas [FA21-BCS-024]"
    ),
).pack()

root.mainloop()

# Wasif Ali
