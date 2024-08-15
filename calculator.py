import tkinter as tk
from tkinter import messagebox

def click(button):
    current = entry.get()
    if button == "AC":
        entry.delete(0, tk.END)
    elif button == "=":
        try:
            result = eval(current.replace('x', '*'))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button)

root = tk.Tk()
root.title("Calculator")


entry = tk.Entry(root, width=20, font=("Arial", 24), bd=8, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    "(", ")", "%", "AC",
    "7", "8", "9", "/",
    "4", "5", "6", "x",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 18), command=lambda b=button: click(b)).grid(row=row, column=col, pady=5, padx=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
