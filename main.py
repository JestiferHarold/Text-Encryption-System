45
from utilities import *
from keys import *
from components import *

def HomePage():
    
    page = Page(App)
    page.addTitle("This is kinda gay")

    buttonPanel = ButtonPanel(page, 2)
    buttonPanel.place(relx = 0.5, y = 15, anchor = "center")

    button = buttonPanel.buttons[0]
    button.config(text = "Sign Up", command = SignUpPage)

    button = buttonPanel.buttons[1]
    button.config(text = "Login ", command = App.showPage())
    return page

def SignUpPage():
    sup = Page(App)
    sup.addTitle("Sign Up")

    TextBoxFor = Canvas(
        sup,
        height = 50,
        width = 100
    ).place(relx = 0, y = 0 )

    userName = StringVar(value = "UserName")
    Email = StringVar(value = "Email")
    Password = StringVar(value = "Password")

    userNameEntry = Entry(
        TextBoxFor,
        textvariable = userName
    ).place(x = 10 , y = 100)

    EmailEntry = Entry(
        TextBoxFor,
        textvariable = Email
    ).place(x = 10, y = 50)

    PasswordEntry = Entry(
        TextBoxFor,
        textvariable = Password
    ).place(x = 10, y = 10)

    button = Button(TextBoxFor, "Submit")
    button.command = print(userName.get(), Email.get(), Password.get())
    button.place(x = 200, y = 10)

    # EmailTextBox = Canvas(
    #     sup,
    #     height = 50,
    #     width = 100
    #     # ANCHOR = "center"       
    # )

    # passwordTextBox = Canvas(
    #     sup,
    #     height = 50,
    #     width = 100,
    #     ANCHOR = "center"       
    # )    

    # addUser()

    return sup

def LoginInPage():
    lip = Page(App)
    lip.addTitle("Login Page")
    
    canvas = Canvas(
        lip,
        height = 50,
        width = 100
    ).place(x = 100, y = 50)

    userName = StringVar(value = "UserName")
    Password = StringVar(value = "Password")

    userNameEntry = Entry(
        canvas,
        textvariable = userName
    ).place(x = 10 , y = 100)

    PasswordEntry = Entry(
        canvas,
        textvariable = Password
    ).place(x = 50, y = 10)

    button = Button(
        canvas,
        "Log in"
    ).place(x = 100, y = 100)
    return lip

def ChangePasswordPage():
    return Page()

def Dashboard():
    dash = Page(App)
    dash.addTitle("DashBoard")

    buttonp = ButtonPanel(dash, 3)
    buttonp.place(x = 100, y = 0)

    button = buttonp.buttons[0]
    button.config(text = "assd")

    encrypingData = StringVar(value = "Enter your data")
    
    canvas = Text(
        dash
        # textvariable = encrypingData.get()
    ).place(x = 300, y = 50)

    button = Button(
        dash
    ).place(x = 10, y = 10)
    
    return dash

def encryptionPage():

    page = Page(App)
    page.addTitle("Here's your cypher")
    page.place(x = 0, y = 0)

    backButton = Button(page, "Back")
    copyButton = Button(page, "Copy")
    exportToFilebutton = Button(page, "Export to a File")
    
    backButton.config()
    backButton.place(x = 100, y = 100)

    copyButton.config()
    copyButton.place(x = 100, y = 120)

    exportToFilebutton.config()
    exportToFilebutton.place(x = 100, y = 140)

    return page


def decryptionPage():
    page = Page(App)
    page.addTitle("Decryption Page")
    page.place(x = 0, y = 0)

    backButton = Button(page, "Back")
    copyButton = Button(page, "Copy")
    exportToFilebutton = Button(page, "Export to a File")
    
    backButton.config()
    backButton.place(x = 100, y = 100)

    copyButton.config()
    copyButton.place(x = 100, y = 120)

    exportToFilebutton.config()
    exportToFilebutton.place(x = 100, y = 140)

    return page

def ExportToAFile():
    page = Page(App)
    page.addTitle("Export to a file")
    # page.place(x = 0, y = 0)

    enter = Entry(
        page,
        textvariable = "FileName"
    )

    enter.place(x = 100, y = 100)
    
    submit = Button(page)
    submit.config(text = "Export", command = lambda : createAFile(enter.get(), "asd"))
    submit.place(x = 150, y = 150)

    return page

    # var = StringVar(value = "")

def deleteAccountPage():
    return Page()


App = Window()

pages = (HomePage, SignUpPage, LoginInPage, ChangePasswordPage, Dashboard, encryptionPage,decryptionPage, deleteAccountPage)

App.registerPage(ExportToAFile())

for page in pages:
    # App.registerPage(page(
    pass
App.mainloop()
# Window().mainloop()