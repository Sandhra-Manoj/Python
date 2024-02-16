import tkinter as tk
def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.geometry("500x500")
root.title("Calculator")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]
def button_click(value):
    if value == '=':
        calculate()
    elif value == 'C':
        clear()
    else:
        entry.insert(tk.END, value)

row, col = 1, 0
for button in buttons:
    tk.Button(root, text=button, font=("Arial", 20),justify='center',
              command=lambda b=button: button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
