import tkinter as tk
from tkinter import _Padding, font
from tkinter.constants import ANCHOR, CENTER
from typing import Text
import openpyxl as op  # For Working with Excel File
from tkinter import Canvas, Grid, mainloop, messagebox, ttk
from tkinter import Frame
import time as t
from PIL import ImageTk, Image
# Pillow Module for image prcoessing
from openpyxl.worksheet.dimensions import ColumnDimension, RowDimension

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
    cnic = sheet.cell(row=row, column=3).value
    balance = sheet.cell(row=row, column=4).value
    account_type = sheet.cell(row=row, column=6).value
    occupation = sheet.cell(row=row, column=7).value
    image = sheet.cell(row=row, column=8).value

    return {
        "name": name,
        "age": age,
        "cnic": cnic,
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
    plate = Canvas(credits_window, height=300, width=300)
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
                    text=f"CNIC: {get_user_info(row)['cnic']}",
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
                    main_window, text="Withdraw Money", padding=20, command=lambda: withdraw_cash()).place(x=25, y=250)
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
    label = tk.Label(new_window, text="Enter account no", pady=200)
    label.place(relx=.5, rely=.7, anchor='center')
    textbar = tk.Entry(new_window).place(x=25, y=67)


def withdraw_cash():
    new_window = tk.Toplevel(root)
    label = tk.Label(new_window, text='Enter amount', bg="white",
                     fg="black", font=("helvtica", 12, font.BOLD), pady=20)
    label.place(relx=.5, rely=.5, anchor="center")
    textbar = tk.Entry(new_window).place(x=225, y=230)

# Creating The Window Where User Will Enter Passcode


def passcode_window():
    passcode_window = tk.Toplevel(root)
    passcode_window.wm_geometry("300x200")
    passcode_window.resizable(False, False)
    plate = Canvas(passcode_window, height=200, width=300)
    label1 = tk.Label(plate, text="Insert Your Passcode", font=("Arial, 16"))
    label1.pack(pady=10)
    passcode = tk.StringVar()
    entry_passcode = ttk.Entry(plate, textvariable=passcode)
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

btn_login = tk.Button(
    frame, text="Login", padx=40, pady=10, command=lambda: passcode_window()
).pack(pady=10)


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
