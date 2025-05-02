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
    button.config(text = "Sign Up", command = lambda : App.showPage(1))

    button = buttonPanel.buttons[1]
    button.config(text = "Login", command = lambda : App.showPage(2))
    
    mainText = Text(page, text = "Confiendtial")
    mainText.place(relx = 0.5, y = 300, anchor = "center")

    # label = Canvas(page)
    # label.place(x = 555, y = 500)
    # labelslider = TypingLabel(page, ["Confidential", encrypt("Confidential")])
    # labelslider.animate()

    return page

def SignUpPage():
    sup = Page(App)
    sup.addTitle("Sign Up")

    TextBoxFor = Canvas(
        sup,
        height = 300,
        width = 400,
        borderwidth = 0
        # bg="#ffffff"
    )

    TextBoxFor.place(relx = 0.5, y = 300, anchor = "center")
    # TextBoxFor.focus_set()

    userName = StringVar(value = "UserName")
    Email = StringVar(value = "Email")
    Password = StringVar(value = "Password")

    userNameEntry = InputBox(
        TextBoxFor,
        userName
    )
    userNameEntry.place(relx = 0.5 , y = 100, anchor = "center")

    userNameEntry.focus_set()

    EmailEntry = InputBox(
        TextBoxFor,
        Email
    )
    EmailEntry.place(relx = 0.5, y = 150, anchor = "center")

    PasswordEntry = InputBox(
        TextBoxFor,
        Password
    )
    PasswordEntry.place(relx = 0.5, y = 200, anchor = "center")

    button = Button(TextBoxFor, "Submit")
    button.command = lambda : back.addUser(userName.get(), email.get(), Password.get())
    button.place(relx = 0.5, y = 250, anchor = "center")

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
    )
    userNameEntry.place(x = 10 , y = 100)

    PasswordEntry = Entry(
        canvas,
        textvariable = Password
    )
    PasswordEntry.place(x = 50, y = 10)

    button = Button(
        canvas,
        "Log in"
    )

    button.command = lambda : back.checkIfUsersExists(userName.get(), Password.get())

    button.place(x = 100, y = 100)

    return lip

def Dashboard():
    dash = Page(App)
    dash.addTitle("DashBoard")

    buttonpanel = ButtonPanel(dash, 5)
    buttonpanel.place(relx = 0.5, y = 150, anchor = "center")

    for index, (name, func) in enumerate([(
        "Encrypt",
        lambda : App.showPage(4)
    ), (
        "Decrypt",
        lambda : App.showPage(5)

    ), (
        "HOME",
        lambda : App.showPage(0)
    ), (
        "Settings",
        lambda : App.showPage(3)
    ), (
        "Exit",
        lambda : exit()
    )]):
        buttonpanel.buttons[index].config(text = name, command = func)
        # buttonpanel.buttons[index].config(command =  work[1])

    encrypingData = StringVar(value = "Enter your data")
    
    Box = Canvas(dash)
    

    return dash

def encryptionPage():

    page = Page(App)
    page.addTitle("Encryption")

    TypeBox = EntryBox(
        page
    )

    TypeBox.config(
        width = 80,
        height = 15,
        borderwidth = 0
    )

    TypeBox.place(relx = 0.5, y = 300, anchor = "center")

    resetButton = Button(page, text = "Reset")
    resetButton.config(command = lambda : TypeBox.delete("1.0", "end"))
    resetButton.place(x = 575, y = 520)

    encryptButton = Button(page, text = "Encrypt")
    # encryptButton.config(width = 200)
    encryptButton.place(x = 1065, y = 520)

    backButton = Button(page, text = "Back")
    backButton.config(command = lambda : App.showPage(3))
    backButton.place(x = 77, y = 520)

    TypeBox.focus_set()

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

    resetButton = Button(page, text = "Reset")
    resetButton.config(command = lambda : TypeBox.delete("1.0", "end"))
    resetButton.place(x = 575, y = 520)

    encryptButton = Button(page, text = "Decrypt")
    # encryptButton.config(width = 200)
    encryptButton.place(x = 1065, y = 520)

    backButton = Button(page, text = "Back")
    backButton.config(command = lambda : App.showPage(3))
    backButton.place(x = 77, y = 520)

    return page

def ExportToAFile():
    page = Page(App)
    page.addTitle("Export to a file")

    buttonPanel = ButtonPanel(
        page,
        5,
        size = 110
    )

    buttonPanel.place(relx = 0.5, y = 450, anchor = "center")

    for index, work in enumerate(((
        "Back",
        lambda : App.showPage()
    ), ("HOME"), ("DashBoard"), ("Copy"), ("Export To File"))):
        buttonPanel.buttons[index].config(text = work)



    return page

def deleteAccountPage():
    return Page()

def ChangePasswordPage():
    return Page()

load_dotenv()

back = Database("root", "2012")

folderName = ""

App = Window()

pages = (HomePage, SignUpPage, LoginInPage, Dashboard, encryptionPage, decryptionPage)

for page in pages:
    App.registerPage(page())

back.createDatabase()

back.createTable()

back.checkIfUsersExists()

back.createAccountsFolder()

back.checkAllAccounts()

back.unlockAllFiles()

App.showPage(3)
App.mainloop()