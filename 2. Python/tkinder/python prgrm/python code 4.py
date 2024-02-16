import tkinter as tk
root=tk.Tk()
root.geometry("800x500")
frame=tk.Frame(root,width=1000, height=500, bg="lightblue")

label=tk.Label(frame, text="label inside frame")
button=tk.Button(frame, text="Button inside frame")


label.pack()
button.pack()
frame.pack()
root.mainloop()