import tkinter as tk
from tkinter import messagebox

expenses = []
amounts = []

def add_expense():
    name = name_entry.get()
    amount = amount_entry.get()
    
    if name == "" or amount == "":
        messagebox.showwarning("Error", "Please fill both fields!")
        return
    
    try:
        amt = int(amount)
        expenses.append(name)
        amounts.append(amt)
        name_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        update_list()
        messagebox.showinfo("Success", "Expense added! ✅")
    except:
        messagebox.showwarning("Error", "Amount must be a number!")

def update_list():
    listbox.delete(0, tk.END)
    for i in range(len(expenses)):
        listbox.insert(tk.END, expenses[i] + " - Rs." + str(amounts[i]))
    
    if len(amounts) > 0:
        total_label.config(text="Total: Rs." + str(sum(amounts)))
    else:
        total_label.config(text="Total: Rs.0")

# Window setup
window = tk.Tk()
window.title("Expense Tracker")
window.geometry("400x600")
window.configure(bg="#1a1a2e")

# Title
tk.Label(window,
    text="Expense Tracker",
    font=("Arial", 22, "bold"),
    bg="#1a1a2e",
    fg="#e94560").pack(pady=20)

# Name input
tk.Label(window,
    text="Expense Name:",
    font=("Arial", 11),
    bg="#1a1a2e",
    fg="white").pack()

name_entry = tk.Entry(window,
    font=("Arial", 12),
    width=25,
    bg="#16213e",
    fg="white",
    insertbackground="white")
name_entry.pack(pady=5)

# Amount input
tk.Label(window,
    text="Amount (Rs.):",
    font=("Arial", 11),
    bg="#1a1a2e",
    fg="white").pack()

amount_entry = tk.Entry(window,
    font=("Arial", 12),
    width=25,
    bg="#16213e",
    fg="white",
    insertbackground="white")
amount_entry.pack(pady=5)

# Add button
tk.Button(window,
    text="Add Expense",
    font=("Arial", 12, "bold"),
    bg="#e94560",
    fg="white",
    width=20,
    command=add_expense).pack(pady=15)

# Expense list
tk.Label(window,
    text="Your Expenses:",
    font=("Arial", 11),
    bg="#1a1a2e",
    fg="white").pack()

listbox = tk.Listbox(window,
    font=("Arial", 11),
    width=35,
    height=8,
    bg="#16213e",
    fg="white",
    selectbackground="#e945c3")
listbox.pack(pady=10)

# Total label
total_label = tk.Label(window,
    text="Total: Rs.0",
    font=("Arial", 14, "bold"),
    bg="#1a1a2e",
    fg="#6bff6b")
total_label.pack(pady=10)

window.mainloop()