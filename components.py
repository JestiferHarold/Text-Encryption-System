from tkinter import *

FONT_LARGE = ("Century Gothic", 35)
FONT_SMALL = ("Century Gothic", 18)
FONT_TOOLTIP = ("Century Gothic", 10)
FONT_BUTTON = ("Century Gothic", 12)
FONT_TEXT = ("Lucida Console", 23)

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

    def showPage(this, index = 1):
        print(this.pages)
        this.pages[index].tkraise()
        this.currentPage = index

class Page(Frame):
    
    def __init__(self, parent):

        super().__init__(parent, width = "1200", height = "900")
        self.fieldCount = 0
        self.textbox = None

    def addTitle(self, title):
        self.title = title

        label = Label(
            self,
            text = title,
            font = FONT_LARGE,
            bg = "#1a1a1f",
            fg = "#e14646"      
        )

        label.place(relx = 0.5, y = 60, anchor = "center")

    def addField(self, title, value):
        
        x = self.fieldCount * 200 + 100
        self.fieldCount += 1
        field = Frame(
            self, 
            height = 100,
            width = 200
        )

        Label(
            field,
            text = title,
            font = 'asd',
            bg="#1a1a1f",
            fg="#e14646"
        ).place(y = 0)

        Label(
            field,
            text = value,
            font = "asd",
            bg="#1a1a1f",
            fg="#e14646"
        ).place(y = 35)

        field.place(x = x, y = 150)

class Button(Button):

    def __init__(self, parent, text = "", state = "normal" ):
        
        super().__init__(
            parent,
            text = text,
            font = "asdad",
            bg = "#111114",
            fg = "#51515b",
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            disabledforeground = "#ffffff",
            activebackground = "#111114",
            activeforeground = "#a1a1ab",
            state = state
        )

class ButtonPanel(Frame):
    
    def __init__(self, parent, buttons, size = 100):
        
        width = buttons * size
        super().__init__(parent, width = width , height = 40, bg = "#111114")
        
        self.buttons = []
        for i in range(buttons):
            button = Button(self)

            self.buttons.append(button)

        x = 0

        for button in self.buttons:
            button.place(height = 40, width = 100, x = x)
            x += size

class TextBox(Canvas):
    def __init__(self, frame):

        super().__init__(frame, height = 300, width = 900)
        self.place(relx = 0.5, y = 400, anchor = "center")
        self.root = self.master.master
        self.master.textbox = self

class EntryBox(Text):

    def __init__(self, frame, textVariable = "", state = "normal"):

        super().__init__(
            frame,
            bg = "#111114",
            fg = "#51515b",
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            # disabledforeground = "#ffffff",
            # activebackground = "#111114",
            # activeforeground = "#a1a1ab",
            state = state,
            font = FONT_SMALL   
        )


class Text(Label):
    def __init__(self, master, text = "", state = "normal"):

        super().__init__(
            master, 
            text = text,
            font = FONT_TEXT,
            # bg = "#111114",
            fg = "#51515b",
            state = state
        )

    def bob(self):
        pass

class InputBox(Entry):

    def __init__(self, frame, text = "", height = 20):
        super().__init__(frame, textvariable = text, width = 30, borderwidth = 0.1, foreground = "#e14646", font = ("Century Gothic", 12))


class TypingLabel:
    def __init__(self, label):
        self.encrypted = label.get()

    def animate(self):
        pass
