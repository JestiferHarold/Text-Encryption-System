from tkinter import *

class Window(Tk):

    def __init__(this):
    
        super().__init__()
        
        this.title('Title')
        this.geometry("1200x600")
        this.resizable(width=False, height=False)

        this.pages = []

    def addPage():
        pass
Window().mainloop()