# -*- coding: utf-8 -*-
from movie import get_all_down_url_list
from tkinter import *
from tkinter.ttk import *

class Application(Frame):
    __slots__ = ['movie_entry', 'search_btn', 'entry_style', 'btn_style']

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.movie_entry = Entry(self)
        self.movie_entry.pack(side="top")

        self.quit = Button(self, text="搜索", command=self.say_hi)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = Tk()
app = Application(master=root)
app.mainloop()