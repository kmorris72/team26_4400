from tkinter import *
import MySQLdb as sql
from LoginWindow import LoginWindow
from OwnerRegistrationWindow import OwnerRegistrationWindow
from VisitorRegistrationWindow import VisitorRegistrationWindow


class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.db = sql.connect(host="academic-mysql.cc.gatech.edu",
                              user="cs4400_team_26",
                              passwd="YFxUWSqD",
                              db="cs4400_team_26")
        
        self.db_cursor = self.db.cursor()

        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)

        self.windows = {}

        for W in (LoginWindow, OwnerRegistrationWindow, VisitorRegistrationWindow):
            window = W(container, self.db_cursor)
            self.windows[W] = window
        
        self.show_window(LoginWindow)
        

    def show_window(self, window):
        self.windows[window].pack()


app = App()
app.mainloop()
