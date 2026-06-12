import random
import string
from tkinter import *
from tkinter import messagebox


def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Password length must be greater than 0."
            )
            return

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ""

        for _ in range(length):
            password += random.choice(characters)

        password_var.set(password)

        if length < 8:
            strength_label.config(
                text="Strength: Weak"
            )

        elif length < 12:
            strength_label.config(
                text="Strength: Medium"
            )

        else:
            strength_label.config(
                text="Strength: Strong"
            )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number."
        )


def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard."
    )


root = Tk()

root.title("Password Generator")
root.geometry("500x300")
root.resizable(False, False)

title = Label(
    root,
    text="Password Generator",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

Label(
    root,
    text="Enter Password Length",
    font=("Arial", 12)
).pack()

length_entry = Entry(
    root,
    font=("Arial", 12)
)

length_entry.pack(pady=5)

Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 12)
).pack(pady=10)

password_var = StringVar()

password_entry = Entry(
    root,
    textvariable=password_var,
    font=("Arial", 12),
    width=40,
    justify="center"
)

password_entry.pack(pady=10)

Button(
    root,
    text="Copy Password",
    command=copy_password,
    font=("Arial", 12)
).pack()

strength_label = Label(
    root,
    text="Strength: -",
    font=("Arial", 12)
)

strength_label.pack(pady=15)

root.mainloop()
