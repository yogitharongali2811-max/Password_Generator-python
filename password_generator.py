import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    length = length_entry.get()

    if not length.isdigit():
        messagebox.showerror("Error", "Enter valid password length")
        return

    length = int(length)

    characters = string.ascii_letters + string.digits
    password = ""

    for i in range(length):
        password += random.choice(characters)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


def reset_fields():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


def accept_password():
    if password_entry.get() == "":
        messagebox.showwarning("Warning", "Generate password first!")
    else:
        messagebox.showinfo("Success", "Password Accepted!")


# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x400")
root.configure(bg="lightgray")


# Title
title = tk.Label(root,
                 text="Password Generator",
                 font=("Arial", 22, "bold"),
                 fg="blue",
                 bg="lightgray")
title.grid(row=0, column=0, columnspan=2, pady=20)


# Username
tk.Label(root,
         text="Enter user name:",
         font=("Arial", 12),
         bg="lightgray").grid(row=1, column=0, padx=20, pady=10, sticky="e")

username_entry = tk.Entry(root, width=30, font=("Arial", 12))
username_entry.grid(row=1, column=1, padx=20)


# Password Length
tk.Label(root,
         text="Enter password length:",
         font=("Arial", 12),
         bg="lightgray").grid(row=2, column=0, padx=20, pady=10, sticky="e")

length_entry = tk.Entry(root, width=30, font=("Arial", 12))
length_entry.grid(row=2, column=1, padx=20)


# Generated Password
tk.Label(root,
         text="Generated password:",
         font=("Arial", 12),
         bg="lightgray").grid(row=3, column=0, padx=20, pady=10, sticky="e")

password_entry = tk.Entry(root,
                          width=30,
                          font=("Arial", 12),
                          fg="green")
password_entry.grid(row=3, column=1, padx=20)


# Generate Button
generate_btn = tk.Button(root,
                         text="GENERATE PASSWORD",
                         font=("Arial", 12, "bold"),
                         bg="darkblue",
                         fg="white",
                         width=22,
                         command=generate_password)

generate_btn.grid(row=4, column=0, columnspan=2, pady=20)


# Accept Button
accept_btn = tk.Button(root,
                       text="ACCEPT",
                       font=("Arial", 12),
                       width=15,
                       command=accept_password)

accept_btn.grid(row=5, column=0, columnspan=2, pady=5)


# Reset Button
reset_btn = tk.Button(root,
                      text="RESET",
                      font=("Arial", 12),
                      width=15,
                      command=reset_fields)

reset_btn.grid(row=6, column=0, columnspan=2, pady=5)


root.mainloop()
