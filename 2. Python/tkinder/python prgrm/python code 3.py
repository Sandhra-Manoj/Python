import tkinter as tk
root=tk.Tk()
root.geometry("800x500")
checkbox=tk.Checkbutton(root, text="option 1")
radio_button1=tk.Radiobutton(root, text="option 2")
radio_button2=tk.Radiobutton(root, text="option 3")
checkbox.pack()
radio_button1.pack()
radio_button2.pack()
root.mainloop()