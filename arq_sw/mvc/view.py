from abc import abstractmethod, ABC
from typing import List, Self
from tkinter import Button, END, Entry, Frame, Label, messagebox, Tk

import controller
from model import Attendant
from util import init_logger


class View(ABC):
    def __init__(self: Self) -> None:
        self._logger = init_logger(log_type='normal')

    @property
    def logger(self):
        return self._logger

    @abstractmethod
    def alert(self, title: str, msg: str) -> None:
        ...

    @abstractmethod
    def update(self) -> None:
        ...

    @abstractmethod
    def mainloop(self) -> None:
        ...


class ViewCli(View):
    def alert(self, title: str, msg: str) -> None:
        print(f'[{title}] {msg}')

    def update(self) -> None:
        print("\n=== ALURA'S SALES MANAGEMENT ===")
        attendants: List[Attendant] = controller.get_all()

        if not attendants:
            print('Empty attendants')
        else:
            for index, attendant in enumerate(attendants, start=1):
                print(f'{index} - {attendant}')

        print('---------------- </ATTENDANTS> ----------------')

    def mainloop(self: Self) -> None:
        self.update()
        print('Instructions:')
        print('<NAME>                 -> add an attendent')
        print('<INDEX>+               -> increment sales. Eg.: 2+')
        print('q or quit or e or exit -> exit this program')

        while True:
            command: str = input('> ').strip()

            if not command:
                continue

            if command.lower() in ['q', 'quit', 'e', 'exit']:
                print('Bye!!')
                break

            if command.endswith('+') and command[:-1].isdigit():
                attendants: List[Attendant] = controller.get_all()
                attendant: Attendant = attendants[int(command[:-1]) - 1]
                self.logger.info(f'{attendant.name=}')
                controller.sales(name=attendant.name)
            else:
                controller.add(command)


class ViewTk(View):
    def __init__(self: Self) -> None:
        super(ViewTk, self).__init__()

        self.__window: Tk = Tk()
        self.__window.title('Alura Sales - MVC')

        self.__entry: Entry = Entry(self.__window)
        self.__entry.pack(pady=5)

        self.__btn_add = Button(self.__window, text='Add Attendant', command=lambda: (controller.add(name=self.__entry.get().strip(), sales=0), self.__entry.delete(0, END)))
        self.__btn_add.pack()

        self.__btn_reset = Button(self.__window, text='Reset Attendants', command=lambda: controller.reset())
        self.__btn_reset.pack()

        self.__frame: Frame = Frame(self.__window)
        self.__frame.pack(pady=10)

    def alert(self: Self, title: str, msg: str) -> None:
        messagebox.showinfo(title, msg)
        self.logger.info(f'Showed: [{title}] {msg}')

    def update(self: Self) -> None:
        for widget in self.__frame.winfo_children():
            widget.destroy()

        for index, attendant in enumerate(controller.get_all()):
            label: Label = Label(self.__frame, text=f'{attendant}')
            label.grid(row=index, column=-0, sticky='w')

            btn_increment: Button = Button(self.__frame, text='+1', command=lambda: controller.sales(name=attendant.name, sales=1))
            btn_increment.grid(row=index, column=1)

    def mainloop(self: Self) -> None:
        self.__window.mainloop()
