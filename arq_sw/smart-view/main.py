import tkinter as tk
from tkinter import messagebox


attendants = []


def add_attendant():
    name: str = entry_name.get().strip()
    if not name:
        messagebox.showwarning('Name is empty', 'Enter a name')
        return

    if name in [a['name'] for a in attendants]:
        messagebox.showinfo('Name is duplicated', 'Enter ANOTHER name')
        return

    attendants.append({"name": name, "sales": 0})
    entry_name.delete(0, tk.END)
    update_interface()


def reset_attendant():
    if messagebox.askyesno('Reset', 'Are you sure that you waan reset all data!?'):
        attendants.clear()

    update_interface()


def increase_sales(index):
    attendants[index]['sales'] += 1

    update_interface()


def update_interface():
    for widget in frame_attendants.winfo_children():
        widget.destroy()

    for i, attendant in enumerate(attendants):
        text = f'{attendant["name"]}: {attendant["sales"]} vendas'
        label = tk.Label(frame_attendants, text=text)
        label.grid(row=i, column=0, sticky='w')

        add_button = tk.Button(frame_attendants, text="+1", command=lambda index=i: increase_sales(index))
        add_button.grid(row=i, column=1)


window = tk.Tk()
window.title('Alura SmartView - Point of Sales')
entry_name = tk.Entry(window)
entry_name.pack()
entry_name.pack(pady=5)
add_button = tk.Button(window, text='Add Attendant', command=add_attendant)
add_button.pack()
reset_button = tk.Button(window, text='Reset', command=reset_attendant)
reset_button.pack()
frame_attendants = tk.Frame(window)
frame_attendants.pack(pady=10)

update_interface()


window.mainloop()
