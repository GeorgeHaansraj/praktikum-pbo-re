import tkinter as tk
from tkinter import ttk, messagebox

# Dictionary untuk menyimpan data user
user_data = {"Summer": "123"}

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in user_data and user_data[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Username atau Password salah!")

def open_register_window():
    register_window = tk.Toplevel(window)
    register_window.title("Register")
    register_window.minsize(300, 150)

    reg_frame = ttk.Frame(register_window)
    reg_frame.pack(pady=10)

    ttk.Label(reg_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    new_username = ttk.Entry(reg_frame)
    new_username.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(reg_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    new_password = ttk.Entry(reg_frame, show="*")
    new_password.grid(row=1, column=1, padx=5, pady=5)

    def register():
        uname = new_username.get()
        pwd = new_password.get()
        if uname and pwd:
            user_data[uname] = pwd
            messagebox.showinfo("Registration Successful", "You have successfully registered")
            register_window.destroy()
        else:
            messagebox.showerror("Error", "Username dan password tidak boleh kosong!")

    ttk.Button(reg_frame, text="Register", command=register).grid(row=2, column=0, columnspan=2, pady=10)

# UI Login Window
window = tk.Tk()
window.title("Login")
window.minsize(300, 150)

frame = ttk.Frame(window)
frame.pack(pady=10)

ttk.Label(frame, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
username_entry = ttk.Entry(frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
password_entry = ttk.Entry(frame, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Button(frame, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=5)
ttk.Button(frame, text="Register", command=open_register_window).grid(row=3, column=0, columnspan=2)

window.mainloop()
