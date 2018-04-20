from tkinter import *
from tkinter import ttk

class ownermanagapropertyWindow:
    def __init__(self, master):
        self.master = master
        master.title("Unconfirmed Properties")

        self.label = Label(self.master,
                           text="Manage Property",
                           font="Times 32")
        self.label.pack()

        self.container1=Frame(master)
        self.container1.pack()

        self.container1a=Frame(self.container1)
        self.container1a.pack(side=LEFT)

        self.container1aa=Frame(self.container1a)
        self.container1aa.pack(side=LEFT)

        self.namelabel = Label(self.container1aa,
                               text="Name:",
                               font="Times 12")
        self.namelabel.pack()

        self.addlabel = Label(self.container1aa,
                           text="Address:",
                           font="Times 12")
        self.addlabel.pack()

        self.citlabel = Label(self.container1aa,
                           text="City:",
                           font="Times 12")
        self.citlabel.pack()

        self.ziplabel = Label(self.container1aa,
                           text="Zip:",
                           font="Times 12")
        self.ziplabel.pack()

        self.sizlabel = Label(self.container1aa,
                           text="Size (acres):",
                           font="Times 12")
        self.sizlabel.pack()

        self.container1ab=Frame(self.container1a)
        self.container1ab.pack(side=RIGHT)

        self.nameentry = Entry(self.container1ab,
                                font="Times 12",
                                width=12)
        self.nameentry.pack()

        self.addressentry = Entry(self.container1ab,
                                font="Times 12",
                                width=12)
        self.addressentry.pack()

        self.cityentry = Entry(self.container1ab,
                                font="Times 12",
                                width=12)
        self.cityentry.pack()

        self.zipentry = Entry(self.container1ab,
                                font="Times 12",
                                width=12)
        self.zipentry.pack()

        self.sizeentry = Entry(self.container1ab,
                                font="Times 12",
                                width=12)
        self.sizeentry.pack()


        self.container1b=Frame(self.container1)
        self.container1b.pack()

        self.container1ba=Frame(self.container1b)
        self.container1ba.pack(side=LEFT)

        self.typlabel = Label(self.container1ba,
                           text="Type:",
                           font="Times 12")
        self.typlabel.pack()

        self.publabel = Label(self.container1ba,
                           text="Public:",
                           font="Times 12")
        self.publabel.pack()

        self.comlabel = Label(self.container1ba,
                           text="Commercial:",
                           font="Times 12")
        self.comlabel.pack()

        self.idlabel = Label(self.container1ba,
                           text="ID:",
                           font="Times 12")
        self.idlabel.pack()

        self.container1bb=Frame(self.container1b)
        self.container1bb.pack(side=RIGHT)


        self.tkvar2 = StringVar(self.container1bb)
        choices = { 'True','False'}
        self.tkvar2.set('False')

        self.popupMenu2 = OptionMenu(self.container1bb, self.tkvar2, *choices)
        self.popupMenu2.pack()


        self.tkvar1 = StringVar(self.container1bb)
        choices = { 'True','False'}
        self.tkvar1.set('False')

        self.popupMenu1 = OptionMenu(self.container1bb, self.tkvar1, *choices)
        self.popupMenu1.pack()


        self.idnumlabel = Label(self.container1bb,
                           text="ID:",
                           font="Times 12")
        self.idnumlabel.pack()



        self.container2=Frame(master)
        self.container2.pack()

        self.container2a=Frame(self.container2)
        self.container2a.pack(side=LEFT)

        self.container2aa=Frame(self.container2a)
        self.container2aa.pack(side=LEFT)

        self.container2ab=Frame(self.container2a)
        self.container2ab.pack(side=RIGHT)

        self.container2b=Frame(self.container2)
        self.container2b.pack(side=RIGHT)

        self.container2ba=Frame(self.container2b)
        self.container2ba.pack(side=LEFT)

        self.container2bb=Frame(self.container2b)
        self.container2bb.pack(side=RIGHT)


        self.container3=Frame(master)
        self.container3.pack()

        self.container3a=Frame(self.container3)
        self.container3a.pack(side=LEFT)

        self.animlabel = Label(self.container3a,
                           text="Add new Animal:",
                           font="Times 12")
        self.animlabel.pack(side=LEFT, pady=(50,0))

        self.container3ab=Frame(self.container3a)
        self.container3ab.pack(side=RIGHT)

        self.addan_button = Button(self.container3ab,
                                   text="Add Animal to \nProperty",
                                   padx=10,
                                   height=2,width=12)
        self.addan_button.pack(side=LEFT, pady=(55,10),padx=5)



        self.container3b=Frame(self.container3)
        self.container3b.pack(side=RIGHT)

        self.animlabel = Label(self.container3b,
                           text="Add new Crop:",
                           font="Times 12")
        self.animlabel.pack(side=LEFT, pady=(50,0))

        self.container3bb=Frame(self.container3b)
        self.container3bb.pack(side=RIGHT)

        self.addcr_button = Button(self.container3bb,
                                   text="Add Crop to \nProperty",
                                   padx=10,
                                   height=2,width=12)
        self.addcr_button.pack(side=LEFT, pady=(55,10),padx=5)


        self.container4=Frame(master)
        self.container4.pack()

        self.requestlabel = Label(self.container1bb,
                           text="Request crop approval :",
                           font="Times 12")

        self.tkvar1 = StringVar(self.container1bb)
        choices = { 'New crop type...','Animal', 'Fruit', 'Nut',
        			'Flower', 'Vegetable'}
        self.tkvar1.set('New crop type...')

        self.delete_property_button = Button(self.container4,
                                   text="Delete Property",
                                   padx=10,
                                   width = 12)
        self.delete_property_button.pack(side=LEFT, pady=(75,0))

        self.container4b=Frame(self.container4)
        self.container4b.pack(side=RIGHT)

        self.save_button = Button(self.container4b,
                                   text="Save Changes\n(confirm property)",
                                   padx=10,
                                   height=3,width=15)
        self.save_button.pack()

        self.back_button = Button(self.container4b,
                                   text="Back\n(Don't Save or Confirm)",
                                   padx=10,
                                   height=3,width=15)
        self.back_button.pack()







root = Tk()
my_gui = adminmanagepropertywindow(root)
root.mainloop()