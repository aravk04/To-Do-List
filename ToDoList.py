# import statements
# tkinter is used for the GUI
import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get() # gets the task from the input text box
    if task:
        task_listbox.insert(tk.END, task) # add task to list
        task_entry.delete(0, tk.END) # clear the input text box after it is added to the list
    else:
        messagebox.showwarning("Error", "Please enter a valid task") # if they don't enter anything

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0] # get index for selected task
        task_listbox.delete(selected_task_index) # delete the selected task
    except IndexError:
        messagebox.showwarning("Error", "Please select a task") # if they dont select a task

# main method to run the interface
def main():
    global task_listbox, task_entry
    root = tk.Tk() # main application window
    root.title("To Do List")
    frame = tk.Frame(root) # frame widget to hold other widgets
    frame.pack(pady = 10) # adds space between widgets

    task_entry = tk.Entry(frame, width = 50) # makes entry widget with size
    task_entry.pack(side=tk.LEFT, pady = 10) # put it on the left side with padding

    add_task_button = tk.Button(frame, text="Add Task", command=add_task) # add task button the
    # command binds it to the function add task
    add_task_button.pack(side = tk.LEFT) # add to the  left side

    task_listbox = tk.Listbox(frame, width = 60, height = 15)
    task_listbox.pack(pady = 20)

    delete_task_button = tk.Button(frame, text="Delete Task", command=delete_task)
    delete_task_button.pack()

    root.mainloop() # this is to run the application
# check if its being run directly and not as a module
if __name__ == "__main__":
    main()

