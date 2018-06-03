# -*- coding: utf-8 -*-
from movie import get_all_down_url_list
from tkinter import *
from tkinter.ttk import *

class Application(Frame):
    __slots__ = ['movie_entry', 'search_btn', 'entry_style', 'btn_style']

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.entry_style = Style()
        self.entry_style.map("TButton",
    foreground=[('pressed', 'red'), ('active', 'white')],
    background=[('pressed', '!disabled', 'black'), ('active', '#4CAF50')]
    )
        self.create_widgets()

    def create_widgets(self):
        self.movie_entry = Entry(self)
        self.movie_entry.pack(side="top")

        self.quit = Button(self, text="QUIT", command=root.destroy, style="TButton")
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = Tk()
app = Application(master=root)
app.mainloop()