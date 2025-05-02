from utilities import *
from keys import *
from components import *
from dotenv import load_dotenv

def HomePage():
    
    page = Page(App)
    page.addTitle("Text Encryption System")
    buttonPanel = ButtonPanel(page, 2)
    buttonPanel.place(relx = 0.5, y = 150, anchor = "center")


    button = buttonPanel.buttons[0]
    button.config(text = "Sign Up", command = SignUpPage)

    button = buttonPanel.buttons[1]
    button.config(text = "Login", command = lambda : X)
    
    mainText = Text(page, text = "This is what we are fighting for")
    mainText.place(relx = 0.5, y = 300, anchor = "center")
    return page

def SignUpPage():
    sup = Page(App)
    sup.addTitle("Sign Up")

    TextBoxFor = Canvas(
        sup,
        height = 200,
        width = 400,
        bg="#ffffff"
    )

    TextBoxFor.place(relx = 0.5, y = 410, anchor = "center")

    userName = StringVar(value = "UserName")
    Email = StringVar(value = "Email")
    Password = StringVar(value = "Password")

    userNameEntry = EntryBox(
        TextBoxFor,
        userName
    )
    userNameEntry.place(relx = 0.5 , y = 100)

    EmailEntry = EntryBox(
        TextBoxFor,
        Email
    ).place(relx = 0.5, y = 50)

    PasswordEntry = EntryBox(
        TextBoxFor,
        Password
    ).place(x = 0, y = 150)

    button = Button(TextBoxFor, "Submit")
    button.command = lambda : print(userName.get(), Email.get(), Password.get())
    button.place(x = 200, y = 10)

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

    buttonpanel = ButtonPanel(dash, 5)
    buttonpanel.place(relx = 0.5, y = 150, anchor = "center")

    for index, work in enumerate((("Encrpyt"), ("Decrypt"), ("HOME"), ("Settings"), ("Log Out"))):
        buttonpanel.buttons[index].config(text = work)

    encrypingData = StringVar(value = "Enter your data")
    
    Box = Canvas(dash)
    

    return dash

def encryptionPage():

    page = Page(App)
    page.addTitle("Encryption")
    page.place(x = 0, y = 0)

    TypeBox = EntryBox(
        page
    )

    TypeBox.config(
        width = 80,
        height = 15,
        borderwidth = 0
    )

    TypeBox.place(relx = 0.5, y = 300, anchor = "center")
    TextBox.focus_set()

    encryptButton = Button(page, text = "Encrypt")
    # encryptButton.config(width = 200)
    encryptButton.place(x = 1065, y = 520)

    backButton = Button(page, text = "Back")
    backButton.place(x = 77, y = 520)

    return page


def decryptionPage():
    page = Page(App)
    page.addTitle("Decryption")
    page.place(x = 0, y = 0)

    TypeBox = EntryBox(
        page
    )

    TypeBox.config(
        width = 80,
        height = 15,
        borderwidth = 0
    )

    TypeBox.place(relx = 0.5, y = 300, anchor = "center")
    TypeBox.focus_set()

    encryptButton = Button(page, text = "Decrypt")
    # encryptButton.config(width = 200)
    encryptButton.place(x = 1065, y = 520)

    backButton = Button(page, text = "Back")
    backButton.place(x = 77, y = 520)

    return page

def ExportToAFile():
    page = Page(App)
    page.addTitle("Export to a file")

    buttonPanel = ButtonPanel(
        page,
        4,
        size = 110
    )

    buttonPanel.place(relx = 0.5, y = 450, anchor = "center")

    for index, work in enumerate((("Back"), ("HOME"), ("Copy"), ("Export To File"))):
        buttonPanel.buttons[index].config(text = work)

    return page

def deleteAccountPage():
    return Page()


load_dotenv()

# back = Database(getenv("username"), getenv("password"))

App = Window()

pages = (HomePage, SignUpPage, LoginInPage, ChangePasswordPage, Dashboard, encryptionPage,decryptionPage, deleteAccountPage)

App.registerPage(ExportToAFile())

for page in pages:
    # App.registerPage(page(
    pass
App.mainloop()