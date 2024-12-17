#importing tkinter from python library
import tkinter as tk
from tkinter import messagebox

#defining add function for the to-do-list application 
def adding():
    task = task_entry.get()
    if task !="":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("The input you enter is invalid","Please enter a valid input")

#defining delete function for the to-do-list application
def delete():
    try:
        desired_index = task_listbox.curselection()
        task_listbox.delete(desired_index)
    except:
        messagebox.showwarning("please select the task to be delete")

first=tk.Tk()

#creating a title for the to-do-list application
first.title("TO--DO--LIST APPLICATION")

#creating and designing a box for adding and deleting button
task_entry = tk.Entry(first,width = 50)
adding_button = tk.Button(first, text ="Adding task to the list",bg='pink',width = 40,command= adding)
removing_button = tk.Button(first,text ="Remove task from the list",bg='skyblue',width= 50,command=delete)
task_listbox = tk. Listbox(first , width= 50, height = 20,bg='white')
first.configure(bg='black')
#creating a widgets for the to-do-list application
task_entry.pack(pady = 10)
adding_button.pack(pady= 15)
removing_button.pack(pady= 20)
task_listbox.pack(pady=25)

#starting a GUI app
first.mainloop()
