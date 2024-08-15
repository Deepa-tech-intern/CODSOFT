import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")


root = tk.Tk()
root.title("To-Do List")
tk.Label(root, text="TO-DO LIST", fg="#191970", bg="#E6E6FA", font=("Times New Roman", 30, "italic", "bold")).pack(pady=10)
tk.Label(root, text="Enter the task", bg="#E6E6FA").pack()
entry = tk.Entry(root, width=50, bg="#F0FFF0", bd=2, relief="solid", font=("Times New Roman", 16, "italic", "bold"))
entry.pack(pady=20)

# Add Task Button
add_button = tk.Button(root, text="Add Task", width=15, command=add_task, bg="#191970", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=3)
add_button.pack(pady=5)


# Delete Task Button
delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task, bg="#191970", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=3)
delete_button.pack(pady=5)

# Close Button
close_button = tk.Button(root, text="Close", command=root.destroy, width=15, bg="#191970", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=3)
close_button.pack(pady=5)

# Listbox to add task
listbox = tk.Listbox(root, width=50, height=20, bg="#F0FFF0", bd=2, relief="solid", font=("Times New Roman", 16, "italic", "bold"))
listbox.pack(pady=20)

root.geometry("650x650")
root.config(bg="#E6E6FA")
root.mainloop()
