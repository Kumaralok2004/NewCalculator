import tkinter as tk

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)


def equal_press():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


root = tk.Tk()
root.title("Calculator")
root.geometry("370x410")

expression = ""
equation = tk.StringVar()

display = tk.Entry(root, textvariable=equation, font=("Arial", 20), justify='right', bd=10, insertwidth=4)
display.grid(columnspan=4, ipadx=10, ipady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 1, 0
for button_text in buttons:
    if button_text == '=':
        button = tk.Button(root, text=button_text, command=equal_press, font=("Arial", 18), height=2, width=5)
    elif button_text == 'C':
        button = tk.Button(root, text=button_text, command=clear, font=("Arial", 18), height=2, width=5)
    else:
        button = tk.Button(root, text=button_text, command=lambda text=button_text: press(text), font=("Arial", 18), height=2, width=5)
    
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
