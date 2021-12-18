import tkinter as tk
from tkinter import Button, messagebox
from tkinter import ttk
from tkinter import font
from tkinter.constants import ANCHOR, CENTER, X
from typing import Text
import openpyxl as op  # For Working with Excel File
import time as t
from PIL import ImageTk, Image
# Pillow Module for image prcoessing

wb = op.load_workbook("users_info.xlsx", read_only=True)
sheet = wb.worksheets[0]


def passcode_available(code):
    row = 1
    while row <= sheet._max_row:
        if sheet.cell(row=row, column=5).value == code:
            return True, row
        else:
            row += 1
    else:
        return False


def get_user_info(row: int):
    name = sheet.cell(row=row, column=1).value
    age = sheet.cell(row=row, column=2).value
    account = sheet.cell(row=row, column=3).value
    balance = sheet.cell(row=row, column=4).value
    account_type = sheet.cell(row=row, column=6).value
    occupation = sheet.cell(row=row, column=7).value
    image = sheet.cell(row=row, column=8).value

    return {
        "name": name,
        "age": age,
        "account": account,
        "balance": balance,
        "account_type": account_type,
        "occupation": occupation,
        "image": image,
    }


# Defining the functions for creating new windows


def credits_window(dev1, dev2):
    credits_window = tk.Toplevel(root)
    credits_window.wm_geometry("400x200")
    credits_window.resizable(False, False)
    plate = tk.Canvas(credits_window, height=300, width=300)
    label1 = tk.Label(
        plate, text="Developers Of The Project:", font=("Arial, 16"))
    label1.pack(pady=10)

    names_lbl = tk.Label(
        plate, text=f"Presented By:\n\n1. {dev1}\n       2. {dev2}")
    names_lbl.pack(pady=10)
    teach_lbl = tk.Label(plate, text=f"Submitted To: Miss Beenish Noor")
    teach_lbl.pack(pady=5)

    plate.pack()


# Getting all the user's data and displaying it on the main window

def proceed(password):

    try:
        password = int(password)
        if password > 999 and password <= 9999:
            if passcode_available(password)[0]:
                row = passcode_available(password)[1]
                main_window = tk.Toplevel(root, bg="#97BFB4")
                main_window.wm_geometry("700x500")
                main_window.resizable(False, False)
                welcome_label = tk.Label(
                    main_window,
                    font=("arial, 18"),
                    text=f"Welcome To The ATM System!",
                    bg="#97BFBF",
                )
                welcome_label.place(x=25, y=25)
                name_label = tk.Label(
                    main_window,
                    text=f"Name: {get_user_info(row)['name']}",
                    bg="#97BFBF",
                    font=("arial, 14"),
                ).place(x=25, y=75)
                age_label = tk.Label(
                    main_window,
                    text=f"Age: {get_user_info(row)['age']}",
                    bg="#97BFBF",
                    font=("arial, 14"),
                ).place(x=275, y=120)
                cnic_label = tk.Label(
                    main_window,
                    text=f"Account no: {get_user_info(row)['account']}",
                    bg="#97BFBF",
                    font=("arial, 14"),
                ).place(x=25, y=120)
                age_label = tk.Label(
                    main_window,
                    text=f"Balance: {get_user_info(row)['balance']}",
                    bg="#97BFBF",
                    font=("arial, 14"),
                ).place(x=275, y=165)
                age_label = tk.Label(
                    main_window,
                    text=f"Account Type: {get_user_info(row)['account_type']}",
                    bg="#97BFBF",
                    font=("arial, 14"),
                ).place(x=25, y=165)
                age_label = tk.Label(
                    main_window,
                    text=f"Occupation: {get_user_info(row)['occupation']}",
                    bg="#97BFBF",
                    font=("arial, 14"),
                ).place(x=275, y=75)
                img = Image.open(f"./{get_user_info(row)['image']}")
                img = img.resize((180, 200), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                panel = tk.Label(main_window, image=img)
                panel.image = img
                panel.place(x=500, y=40)
                withdraw_btn = ttk.Button(
                    main_window, text="Cash Withdrawal", padding=20, command=lambda: withdraw_cash()).place(x=25, y=250)
                moneytransfer_btn = ttk.Button(
                    main_window, text="Money Transfer", padding=20, command=lambda: money_transfer()).place(x=275, y=250)

        else:
            raise Exception

    except Exception as Error:
        messagebox.showerror(
            title="Error", message="Invalid Credentials",
        )
        print(Error)


def money_transfer():
    new_window = tk.Toplevel(root)
    new_window.geometry("300x500")
    new_window.configure(bg="#FFFAF0")
    label = tk.Label(new_window, text="ENTER ACCOUNT NO", bg="#FFFAF0",
                     fg="black", font=("sans-serif", 16, font.BOLD, font.ITALIC), pady=10)
    label.place(x=40, y=50)
    textbar = tk.Entry(new_window).place(x=55, y=100, height=30, width=175)
    label2 = tk.Label(new_window, text="ENTER AMOUNT", bg="#FFFAF0", fg="black", font=(
        "sans-serif", 16, font.BOLD, font.ITALIC), pady=10)
    label2.place(x=53, y=150)
    textbar = tk.Entry(new_window).place(x=55, y=200, height=30, width=175)
    button = ttk.Button(new_window, text="Proceed", padding=10).place(x=100, y=250)
    label.place(x=55, y=50)
    textbar = tk.Entry(new_window).place(x=75, y=100, height=30, width=175)
    label2 = tk.Label(new_window, text="ENTER AMOUNT", bg="#FFFAF0", fg="black", font=(
        "sans-serif", 16, font.BOLD, font.ITALIC), pady=10)
    label2.place(x=55, y=150)
    textbar = tk.Entry(new_window).place(x=75, y=200, height=30, width=175)
    button = ttk.Button(new_window, text="Proceed",
                        command=lambda: moneytransfer_confirmation()).place(x=100, y=300)


def withdraw_cash():
    new_window = tk.Toplevel(root)
    new_window.geometry("300x500")
    label = tk.Label(new_window, text='ENTER AMOUNT', bg="#FFFAF0",
                     fg="black", font=("sans-serif", 16, font.BOLD, font.ITALIC), pady=10)
    label.place(x=75, y=150)
    new_window.configure(bg="#FFFAF0")
    textbar = tk.Entry(new_window).place(x=75, y=200, height=30, width=150)
    button = ttk.Button(new_window, text="Proceed",
                        command=lambda: withdraw_confirmation()).place(x=100, y=250)


# Creating confirmation window
def withdraw_confirmation():
    new_window = tk.Toplevel(root, bg="#26BABF")
    new_window.geometry("500x500")
    button = ttk.Button(new_window, text="Pay now").place(x=50, y=50)


def moneytransfer_confirmation():
    new_window = tk.Toplevel(root, bg="#26BABF")
    new_window.geometry("500x500")
    Button = ttk.Button(new_window, text="Pay now").place(x=50, y=50)


# Creating The Window Where User Will Enter Passcode


def passcode_window():
    passcode_window = tk.Toplevel(root)
    passcode_window.wm_geometry("300x200")
    passcode_window.resizable(False, False)
    plate = tk.Canvas(passcode_window, height=200, width=300)
    label1 = tk.Label(plate, text="Insert Your Passcode", font=("Arial, 16"))
    label1.pack(pady=10)
    passcode = tk.StringVar()
    entry_passcode = tk.Entry(plate, textvariable=passcode)
    entry_passcode.pack()
    btn_check_passcode = ttk.Button(
        plate, text="OK", command=lambda: proceed(passcode.get()), width=20
    ).pack(pady=10)
    plate.pack(pady=40)


# Creating the main GUI Structure i.e. Root of the program
root = tk.Tk()
root.resizable(False, False)
root.title("ATM System")
# Giving a background canvas to the app

canvas = tk.Canvas(root, height=400, width=400, bg="#B8E4F0")
canvas.pack()

frame = tk.Frame(root, bg="#98BAE7")
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

btn_login = ttk.Button(
    frame, text="Login", padding=10, command=lambda: passcode_window()
).pack(pady=10)


btn_credits = ttk.Button(
    frame,
    padding=10,
    text="About Developers",
    command=lambda: credits_window(
        "Wasif Ali [FA21-BCS-035]", "Marium Ilyas [FA21-BCS-024]"
    ),
).pack()

root.mainloop()

# Wasif Ali
