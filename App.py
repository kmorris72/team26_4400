from tkinter import *   
import MySQLdb as sql
from LoginWindow import LoginWindow
from OwnerRegistrationWindow import OwnerRegistrationWindow
from VisitorRegistrationWindow import VisitorRegistrationWindow
from AdminOwnerOverviewWindow import AdminOwnerOverviewWindow
from AdminViewConfirmedPropertiesWindow import AdminViewConfirmedPropertiesWindow
from AdminVisitorOverviewWindow import AdminVisitorOverviewWindow


# All of the windows that make up the app.
ALL_WINDOWS = (LoginWindow, OwnerRegistrationWindow, VisitorRegistrationWindow, AdminOwnerOverviewWindow, AdminViewConfirmedPropertiesWindow, AdminVisitorOverviewWindow)


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self)

        self.db = sql.connect(host="academic-mysql.cc.gatech.edu",
                              user="cs4400_team_26",
                              passwd="YFxUWSqD",
                              db="cs4400_team_26")
        
        self.db_cursor = self.db.cursor()

        container = Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=True)

        self.windows = {}

        for W in ALL_WINDOWS:
            window = W(container, self.db_cursor)
            self.windows[W.__name__] = window
        
        self.curr_window = "LoginWindow"
        self.show_window(self.curr_window)

    def show_window(self, window):
        self.windows[self.curr_window].pack_forget()
        self.windows[window].pack()
        self.curr_window = window
        

app = App()
app.mainloop()
