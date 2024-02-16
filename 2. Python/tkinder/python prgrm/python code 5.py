import tkinter as tk
def get_selected_item():
    selected_item =listbox.get(tk.ACTIVE)
    print("selected item:", selected_item)
root=tk.Tk()
root.geometry("800x500")
listbox =tk.Listbox(root)
listbox.pack()
for item in ["option1","option2","option3"]:
    listbox.insert(tk.END, item)
button=tk.Button(root, text="Get selected item",command=get_selected_item)
button.pack()
root.mainloop()