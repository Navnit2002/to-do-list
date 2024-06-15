import tkinter as tk
from tkinter import messagebox

# Function to add a new task to the list
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)  # Reset the entry field after adding task
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Function to mark a task as done (delete from the listbox)
def mark_as_done():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")

# Function to clear all tasks from the listbox
def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create the main tkinter window
root = tk.Tk()
root.title("To-Do List")

# Create and pack the task entry and buttons
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

done_button = tk.Button(root, text="Mark as Done", command=mark_as_done)
done_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack(pady=5)

# Create and pack the task listbox
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(padx=10, pady=10)

# Start the tkinter main loop
root.mainloop()
