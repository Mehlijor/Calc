import tkinter as tk


def evaluate(button):
    if button == "=":
        try:
            user_input = entry.get()
            output = eval(user_input)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(output))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button)


# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: evaluate(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the Tkinter event loop
root.mainloop()
