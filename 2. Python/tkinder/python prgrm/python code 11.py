import tkinter as tk
from tkinter import messagebox
def show_message():
    messagebox.showinfo("Info","This is an informational message")
def show_alert():
    messagebox.showwarning("Warning","This is a warning message")
def ask_question():
    response=messagebox.askquestion("Question","Do you want to proceed?")
    if response=="yes":
        print("User wants to proceed.")
    else:
        print("User chose not to proceed.")
root=tk.Tk()
root.geometry("500x500")
info_button=tk.Button(root,text="Show Info",command=show_message)
Warning_button=tk.Button(root,text="Show warning",command=show_alert)
question_button=tk.Button(root,text="Ask Question",command=ask_question)
info_button.pack()
Warning_button.pack()
question_button.pack()
root.mainloop()