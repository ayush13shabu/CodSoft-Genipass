import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()

    if complexity == 'Low':
        characters = string.ascii_lowercase
    elif complexity == 'Medium':
        characters = string.ascii_letters + string.digits
    elif complexity == 'High':
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    password = password_var.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Password Generator", "Password copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

complexity_label = tk.Label(root, text="Complexity Level:")
complexity_label.grid(row=1, column=0, padx=10, pady=5)

complexity_var = tk.StringVar(root)
complexity_var.set("Low")
complexity_dropdown = tk.OptionMenu(root, complexity_var, "Low", "Medium", "High")
complexity_dropdown.grid(row=1, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, state='readonly')
password_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
