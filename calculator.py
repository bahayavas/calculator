import tkinter as tk

screen_text = ""
operation = ""
previous_number = 0

def add_number(value):
    global screen_text
    screen_text += str(value)
    label_screen.config(text=screen_text)

def clear_screen():
    global screen_text
    screen_text = ""
    label_screen.config(text=screen_text)

def select_operation(op):
    global operation, previous_number, screen_text
    operation = op
    previous_number = float(screen_text)
    clear_screen()

def equals():
    global screen_text, previous_number, operation
    new_number = float(screen_text)
    result = 0
    
    if operation == "+":
        result = previous_number + new_number
    elif operation == "-":
        result = previous_number - new_number
    elif operation == "*":
        result = previous_number * new_number
    elif operation == "/":
        if new_number != 0:
            result = previous_number / new_number
            if result.is_integer():
                result = int(result)
        else:
            result = "Error"

    label_screen.config(text=str(result))
    screen_text = str(result)

root = tk.Tk()
root.title('Calculator')
root.geometry('600x600')
root.resizable(False, False)

label_screen = tk.Label(root, text="", fg='white', bg='black', font='Times 24', width=25, height=3, anchor="e")
label_screen.place(x=50, y=50)

button_size = (5,2)  
button_font = 'Times 20'

number_buttons = {
    '7': (50, 180), '8': (150, 180), '9': (250, 180),
    '4': (50, 250), '5': (150, 250), '6': (250, 250),
    '1': (50, 320), '2': (150, 320), '3': (250, 320),
    '0': (150, 390), '.': (250, 390)
}

for num, (x, y) in number_buttons.items():
    tk.Button(root, text=f' {num} ', fg='white', bg='black', font=button_font,
              command=lambda n=num: add_number(n), width=button_size[0], height=button_size[1]).place(x=x, y=y)

tk.Button(root, text=' + ', fg='white', bg='black', font=button_font, command=lambda: select_operation("+"), width=button_size[0], height=button_size[1]).place(x=350, y=180)
tk.Button(root, text=' - ', fg='white', bg='black', font=button_font, command=lambda: select_operation("-"), width=button_size[0], height=button_size[1]).place(x=350, y=250)
tk.Button(root, text=' x ', fg='white', bg='black', font=button_font, command=lambda: select_operation("*"), width=button_size[0], height=button_size[1]).place(x=350, y=320)
tk.Button(root, text=' / ', fg='white', bg='black', font=button_font, command=lambda: select_operation("/"), width=button_size[0], height=button_size[1]).place(x=350, y=390)

tk.Button(root, text=' = ', fg='white', bg='green', font=button_font, command=equals, width=button_size[0], height=button_size[1]).place(x=250, y=460)
tk.Button(root, text='C', fg='white', bg='red', font=button_font, command=clear_screen, width=button_size[0], height=button_size[1]).place(x=50, y=460)

root.mainloop()
