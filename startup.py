# -*- coding: utf-8 -*-
from movie import get_all_down_url_list
from tkinter import *
from tkinter.ttk import *
import asyncio



class Application(Frame):
    __slots__ = ['movie_entry', 'search_btn', 'entry_style', 'btn_style', 'progress_bar', 'root']

    def __init__(self, master=Tk()):
        self.root = master
        self.root.title('Movie Search')      
        super(Application,self).__init__(master)
        self.btn_style = Style()
        self.btn_style.map("Search.TButton",
            foreground = [('disabled','white')],
            background = [('disabled','grey')]
        )
        self.pack()
        self.__create_widgets()
    
    def __call__(self,width=300,height=200):
        self.master.minsize(width,height)      
        self.mainloop()

    def __create_widgets(self):
        self.movie_entry = Entry(self)
        self.movie_entry.pack(side="top")

        self.search_btn = Button(self, text="搜索", command=self.__search_movie,  style="Search.TButton")
        self.search_btn.pack(side="bottom",pady=10)

    def __search_movie(self):
        movie_name = self.movie_entry.get()
        self.__handle_ui_under_search()

    def __get_movie_list(self,movie_name):
        self.movie_list_box = Listbox()
        for movie in get_all_down_url_list(movie_name):
            self.movie_list_box.insert(END, movie)
    
    def __movie_list_select(self,evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        # TODO 复制到剪贴板

    def __handle_ui_after_search(self):
        self.search_btn.config(state=ACTIVE)
        self.progress_bar.destroy()

    def __handle_ui_under_search(self):
        self.search_btn.config(state=DISABLED)
        self.progress_bar = Progressbar(self, orient=HORIZONTAL, mode='indeterminate')
        self.progress_bar.start()
        self.progress_bar.pack(pady=10)

if __name__ == '__main__':
    app = Application()
    app()