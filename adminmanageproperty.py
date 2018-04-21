from tkinter import *
from tkinter import ttk

class adminmanagepropertywindow:
    def __init__(self, master, db_cursor):
        self.master = master
        master.title("Unconfirmed Properties")

        self.db_cursor=db_cursor


        name="""select name from propertylist"""
        self.label = Label(self.master,
                           text="Manage Property",
                           font="Times 32")
        self.label.pack()

        self.basicinfocontainer=Frame(master)
        self.basicinfocontainer.pack()

        self.basicinfocontainerlabelspart1=Frame(self.basicinfocontainer)
        self.basicinfocontainerlabelspart1.pack(side=LEFT)

        self.basicinfocontainerlabelspart1leftside=Frame(self.basicinfocontainerlabelspart1)
        self.basicinfocontainerlabelspart1leftside.pack(side=LEFT)

        self.namelabel = Label(self.basicinfocontainerlabelspart1leftside,
                               text="Name:",
                               font="Times 12")
        self.namelabel.pack()

        self.addlabel = Label(self.basicinfocontainerlabelspart1leftside,
                           text="Address:",
                           font="Times 12")
        self.addlabel.pack()

        self.citlabel = Label(self.basicinfocontainerlabelspart1leftside,
                           text="City:",
                           font="Times 12")
        self.citlabel.pack()

        self.ziplabel = Label(self.basicinfocontainerlabelspart1leftside,
                           text="Zip:",
                           font="Times 12")
        self.ziplabel.pack()

        self.sizlabel = Label(self.basicinfocontainerlabelspart1leftside,
                           text="Size (acres):",
                           font="Times 12")
        self.sizlabel.pack()

        self.basicinfocontainerlabelspart1rightside=Frame(self.basicinfocontainerlabelspart1)
        self.basicinfocontainerlabelspart1rightside.pack(side=RIGHT)

        self.nameentry = Entry(self.basicinfocontainerlabelspart1rightside,
                                font="Times 12",
                                width=12)
        self.nameentry.pack()

        self.addressentry = Entry(self.basicinfocontainerlabelspart1rightside,
                                font="Times 12",
                                width=12)
        self.addressentry.pack()

        self.cityentry = Entry(self.basicinfocontainerlabelspart1rightside,
                                font="Times 12",
                                width=12)
        self.cityentry.pack()

        self.zipentry = Entry(self.basicinfocontainerlabelspart1rightside,
                                font="Times 12",
                                width=12)
        self.zipentry.pack()

        self.sizeentry = Entry(self.basicinfocontainerlabelspart1rightside,
                                font="Times 12",
                                width=12)
        self.sizeentry.pack()


        self.basicinfocontainerlabelspart2=Frame(self.basicinfocontainerlabels)
        self.basicinfocontainerlabelspart2.pack()

        self.basicinfocontainerlabelspart2leftside=Frame(self.basicinfocontainerlabelspart2)
        self.basicinfocontainerlabelspart2leftside.pack(side=LEFT)

        self.typlabel = Label(self.basicinfocontainerlabelspart2leftside,
                           text="Type:",
                           font="Times 12")
        self.typlabel.pack()

        self.publabel = Label(self.basicinfocontainerlabelspart2leftside,
                           text="Public:",
                           font="Times 12")
        self.publabel.pack()

        self.comlabel = Label(self.basicinfocontainerlabelspart2leftside,
                           text="Commercial:",
                           font="Times 12")
        self.comlabel.pack()

        self.idlabel = Label(self.basicinfocontainerlabelspart2leftside,
                           text="ID:",
                           font="Times 12")
        self.idlabel.pack()

        self.basicinfocontainerlabelspart2rightside=Frame(self.basicinfocontainerlabelspart2)
        self.basicinfocontainerlabelspart2rightside.pack(side=RIGHT)

        self.atypelabel = Label(self.basicinfocontainerlabelspart2rightside,
                           text="Farm",
                           font="Times 12")
        self.atypelabel.pack()

        self.tkvar2 = StringVar(self.basicinfocontainerlabelspart2rightside)
        choices = { 'True','False'}
        self.tkvar2.set('False')

        self.popupMenu2 = OptionMenu(self.basicinfocontainerlabelspart2rightside, self.tkvar2, *choices)
        self.popupMenu2.pack()


        self.tkvar1 = StringVar(self.basicinfocontainerlabelspart2rightside)
        choices = { 'True','False'}
        self.tkvar1.set('False')

        self.popupMenu1 = OptionMenu(self.basicinfocontainerlabelspart2rightside, self.tkvar1, *choices)
        self.popupMenu1.pack()


        self.idnumlabel = Label(self.basicinfocontainerlabelspart2rightside,
                           text="ID:",
                           font="Times 12")
        self.idnumlabel.pack()



        self.animalsandcropscontainer=Frame(master)
        self.animalsandcropscontainer.pack()

        self.animalsandcropscontainerpartanimals=Frame(self.animalsandcropscontainer)
        self.animalsandcropscontainerpartanimals.pack(side=LEFT)

        self.animalsandcropscontainerpartanimalslabelsside=Frame(self.animalsandcropscontainerpartanimals)
        self.animalsandcropscontainerpartanimalslabelsside.pack(side=LEFT)

        self.alabel=Label(self.animalsandcropscontainerpartanimalslabelsside,
                        text="Animals:",
                        font="Times 12")


        self.animalsandcropscontainerpartanimalslistside=Frame(self.animalsandcropscontainerpartanimals)
        self.animalsandcropscontainerpartanimalslistside.pack(side=RIGHT)

        self.animalsandcropscontainercropsside=Frame(self.animalsandcropscontainer)
        self.animalsandcropscontainercropsside.pack(side=RIGHT)

        self.animalsandcropscontainercropssidelabelside=Frame(self.animalsandcropscontainercropsside)
        self.animalsandcropscontainercropssidelabelside.pack(side=LEFT)

        self.alabel=Label(self.animalsandcropscontainercropssidelabelside,
                        text="Crops:",
                        font="Times 12")


        self.animalsandcropscontainercropssidelistsside=Frame(self.animalsandcropscontainercropsside)
        self.animalsandcropscontainercropssidelistsside.pack(side=RIGHT)


        self.addanimalsorcropscontainer=Frame(master)
        self.addanimalsorcropscontainer.pack()

        self.addanimalsorcropscontaineraddanimal=Frame(self.addanimalsorcropscontainer)
        self.addanimalsorcropscontaineraddanimal.pack(side=LEFT)

        self.animlabel = Label(self.addanimalsorcropscontaineraddanimal,
                           text="Add new Animal:",
                           font="Times 12")
        self.animlabel.pack(side=LEFT, pady=(50,0))

        self.addanimalsorcropscontaineraddanimalselectside=Frame(self.addanimalsorcropscontaineraddanimal)
        self.addanimalsorcropscontaineraddanimalselectside.pack(side=RIGHT)


        self.tkvar = StringVar(self.addanimalsorcropscontaineraddanimalselectside)

        choices = { 'Select approved animal...','Fruit','Animal','Vegetable','Flower'}
        self.tkvar.set('Select approved animal...')

        self.popupMenu = OptionMenu(self.addanimalsorcropscontaineraddanimalselectside, self.tkvar, *choices)
        self.popupMenu.pack()


        self.addan_button = Button(self.addanimalsorcropscontaineraddanimalselectside,
                                   text="Add Animal to \nProperty",
                                   padx=10,
                                   height=2,width=12)
        self.addan_button.pack(side=LEFT, pady=(5,10),padx=5)



        self.addanimalsorcropscontaineraddcrops=Frame(self.addanimalsorcropscontainer)
        self.addanimalsorcropscontaineraddcrops.pack(side=RIGHT)

        self.animlabel = Label(self.addanimalsorcropscontaineraddcrops,
                           text="Add new Crop:",
                           font="Times 12")
        self.animlabel.pack(side=LEFT, pady=(50,0))

        self.addanimalsorcropscontaineraddcropsselectside=Frame(self.addanimalsorcropscontaineraddcrops)
        self.addanimalsorcropscontaineraddcropsselectside.pack(side=RIGHT)

        self.tkvar2 = StringVar(self.addanimalsorcropscontaineraddcropsselectside)

        choices = { 'Select approved crop...','Name',"Type"}
        self.tkvar2.set('Select approved crop...')

        self.popupMenu2 = OptionMenu(self.addanimalsorcropscontaineraddcropsselectside, self.tkvar2, *choices)
        self.popupMenu2.pack()



        self.addcr_button = Button(self.addanimalsorcropscontaineraddcropsselectside,
                                   text="Add Crop to \nProperty",
                                   padx=10,
                                   height=2,width=12)
        self.addcr_button.pack(side=LEFT, pady=(5,10),padx=5)


        self.deletesavebackbuttonscontainer=Frame(master)
        self.deletesavebackbuttonscontainer.pack()


        self.delete_property_button = Button(self.deletesavebackbuttonscontainer,
                                   text="Delete Property",
                                   padx=10,
                                   width = 12)
        self.delete_property_button.pack(side=LEFT, pady=(75,0))

        self.deletesavebackbuttonscontainermiddlesection=Frame(self.deletesavebackbuttonscontainer)
        self.deletesavebackbuttonscontainermiddlesection.pack(side=RIGHT)

        self.save_button = Button(self.deletesavebackbuttonscontainermiddlesection,
                                   text="Save Changes\n(confirm property)",
                                   padx=10,
                                   height=3,width=15)
        self.save_button.pack()

        self.back_button = Button(self.deletesavebackbuttonscontainermiddlesection,
                                   text="Back\n(Don't Save or Confirm)",
                                   padx=10,
                                   height=3,width=15)
        self.back_button.pack()






root = Tk()
my_gui = adminmanagepropertywindow(root)
root.mainloop()

