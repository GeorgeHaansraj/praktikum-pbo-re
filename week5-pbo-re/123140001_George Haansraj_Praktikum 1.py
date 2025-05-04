import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "Summer" and password == "123":
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Username atau Password salah!")

window = tk.Tk()
window.title("Login")
window.minsize(300, 150)

frame = ttk.Frame(window)
frame.pack(pady=10)

# Label untuk Username dan Password
ttk.Label(frame, text="Username:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
ttk.Label(frame, text="Password:").grid(row=1, column=0, sticky="e", padx=5, pady=5)

# Entry untuk Username dan Password
username_entry = ttk.Entry(frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_entry = ttk.Entry(frame, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Tombol Login
ttk.Button(frame, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()