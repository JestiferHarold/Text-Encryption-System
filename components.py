from tkinter import *

class Window(Tk):

    def __init__(this):
    
        super().__init__()
        
        this.title('Title')
        this.geometry("1200x600")
        this.resizable(width=False, height=False)
        this.tk_setPalette(background="#1a1a1f", foreground="#ffffff")

        this.pages = []

    def registerPage(this, page, index = None):
        if index == None:
            this.pages.append(page)
        else:
            this.pages[index] = page
        page.place(x = 0, y = 0)

    def showPage(this, index):
        this.pages[index].tkraise()
        this.currentPage = index

class Page(Frame):
    pass

Window().mainloop()