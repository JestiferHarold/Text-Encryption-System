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

    
    return sup

def LoginInPage():
    return Page()

def ChangePasswordPage():
    return Page()

def Dashboard():
    return Page()

def encryptionPage():
    return Page()

def decryptionPage():
    return Page()

def deleteAccountPage():
    return Page()


App = Window()

pages = (HomePage, SignUpPage, LoginInPage, ChangePasswordPage, Dashboard, encryptionPage,decryptionPage, deleteAccountPage)

for page in pages:
    App.registerPage(page())

App.mainloop()
# Window().mainloop()