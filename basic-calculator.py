import tkinter as tk
from tkinter import font
from functools import partial


def get_input(entry, argu):
    entry.insert(tk.END, argu)


def backspace(entry):
    entry.delete(len(entry.get()) - 1)


def clear(entry):
    entry.delete(0, tk.END)


def calc(entry):
    input_info = entry.get()
    try:
        output = str(eval(input_info.strip()))
    except ZeroDivisionError:
        popupmsg()
        output = ""
    clear(entry)
    entry.insert(tk.END, output)


def popupmsg():
    popup = tk.Toplevel()
    popup.resizable(0, 0)
    popup.geometry("200x100")
    popup.title("Alert")
    label = tk.Label(popup, text="Cannot divide by 0!\nEnter valid values", font=("Helvetica", 12))
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", bg="#4CAF50", fg="white", font=("Helvetica", 12), command=popup.destroy)
    B1.pack(pady=5)
    popup.mainloop()


def create_button(parent, text, command, color, active_color, size=(4, 2)):
    """Create a 3D effect button."""
    return tk.Button(parent, text=text, font=("Helvetica", 16), fg='white', bg=color, activebackground=active_color,
                     relief='raised', bd=4, command=command, width=size[0], height=size[1])


def cal():
    root = tk.Tk()
    root.title("Calculator")
    root.resizable(0, 0)
    root.configure(bg='#2E2E2E')

    entry_font = font.Font(size=24, weight='bold')
    entry = tk.Entry(root, justify="right", font=entry_font, bd=0, relief='flat', bg='#333', fg='#FFF')
    entry.grid(row=0, column=0, columnspan=4, sticky=tk.N + tk.W + tk.S + tk.E, padx=10, pady=10)

    cal_button_bg = '#FF9800'
    num_button_bg = '#424242'
    other_button_bg = '#757575'
    button_active_bg = '#FF5722'

    # Create buttons with 3D effect
    button7 = create_button(root, '7', lambda: get_input(entry, '7'), num_button_bg, button_active_bg)
    button7.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button8 = create_button(root, '8', lambda: get_input(entry, '8'), num_button_bg, button_active_bg)
    button8.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button9 = create_button(root, '9', lambda: get_input(entry, '9'), num_button_bg, button_active_bg)
    button9.grid(row=1, column=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button4 = create_button(root, '4', lambda: get_input(entry, '4'), num_button_bg, button_active_bg)
    button4.grid(row=2, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button5 = create_button(root, '5', lambda: get_input(entry, '5'), num_button_bg, button_active_bg)
    button5.grid(row=2, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button6 = create_button(root, '6', lambda: get_input(entry, '6'), num_button_bg, button_active_bg)
    button6.grid(row=2, column=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button1 = create_button(root, '1', lambda: get_input(entry, '1'), num_button_bg, button_active_bg)
    button1.grid(row=3, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button2 = create_button(root, '2', lambda: get_input(entry, '2'), num_button_bg, button_active_bg)
    button2.grid(row=3, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button3 = create_button(root, '3', lambda: get_input(entry, '3'), num_button_bg, button_active_bg)
    button3.grid(row=3, column=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button0 = create_button(root, '0', lambda: get_input(entry, '0'), num_button_bg, button_active_bg, size=(8, 2))
    button0.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button13 = create_button(root, '.', lambda: get_input(entry, '.'), num_button_bg, button_active_bg)
    button13.grid(row=4, column=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button14 = create_button(root, '/', lambda: get_input(entry, '/'), cal_button_bg, button_active_bg)
    button14.grid(row=1, column=3, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button11 = create_button(root, '-', lambda: get_input(entry, '-'), cal_button_bg, button_active_bg)
    button11.grid(row=2, column=3, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button12 = create_button(root, '*', lambda: get_input(entry, '*'), cal_button_bg, button_active_bg)
    button12.grid(row=3, column=3, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button10 = create_button(root, '+', lambda: get_input(entry, '+'), cal_button_bg, button_active_bg)
    button10.grid(row=4, column=3, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button18 = create_button(root, '^', lambda: get_input(entry, '**'), cal_button_bg, button_active_bg)
    button18.grid(row=5, column=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button17 = create_button(root, '=', lambda: calc(entry), cal_button_bg, button_active_bg)
    button17.grid(row=5, column=3, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button15 = create_button(root, '<-', lambda: backspace(entry), other_button_bg, button_active_bg)
    button15.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button16 = create_button(root, 'C', lambda: clear(entry), other_button_bg, button_active_bg)
    button16.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    exit_button = create_button(root, 'Quit', root.quit, 'black', '#333', size=(8, 2))
    exit_button.grid(row=6, column=0, columnspan=4, padx=5, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)

    # Create a footer frame
    footer_frame = tk.Frame(root, bg='#2E2E2E')
    footer_frame.grid(row=7, column=0, columnspan=4, sticky=tk.W + tk.E, pady=10)

    # Footer label
    footer_label = tk.Label(footer_frame, text="Application developed by: codewithj4ke", font=("Calibri", 8),
                            bg='#2E2E2E', fg='white')
    footer_label.pack()

    # Set uniform grid row/column weights for resizing
    for i in range(7):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()


if __name__ == '__main__':
    cal()
