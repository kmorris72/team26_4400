from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox


class AdminViewPendingItemsWindow(Frame):
    def __init__(self, master, db_cursor):
        Frame.__init__(self, master)

        self.db_cursor = db_cursor

        self.tablecontainer=Frame(self)
        self.tablecontainer.pack()

        self.label = Label(self.tablecontainer,
                           text="Pending Approval Animals/Crops",
                           font="Times 32")
        self.label.pack()

        self.tree=ttk.Treeview(self, columns=('Name','Type'))
        self.tree.pack()
        self.tree.displaycolumns=("Name","Type")
        self.tree.column("Name", width=100 )
        self.tree.column("Type", width=100)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Type", text="Type")
        self.tree['show'] = 'headings'

        self.button_container = Frame(self)
        self.button_container.pack(pady=40 , padx = 20)

        self.approve_selection_button = Button(self.button_container,
                                   text="Approve \nSelection",
                                   padx=10,
                                   height = 2, width = 12,
                                   command=self.approve_selection_button_clicked_handler)
        self.approve_selection_button.pack(pady = 5, padx = 10)


        self.delete_selection_button = Button(self.button_container,
                                       text="Delete Selection",
                                       padx=10,
                                       command=self.delete_button_clicked_handler)
        self.delete_selection_button.pack(pady = 5, padx = 10,)
        self.back_button = Button(self.button_container,
                                         text="Back",
                                         padx=10,
                                         width=12,
                                         command=self.back_button_clicked_handler)
        self.back_button.pack(pady = 5, padx = 5)


    def approve_selection_button_clicked_handler(self):
        should_approve = messagebox.askyesno("Alert", "Are You Sure You Want to Approve the Selected Item?")
        if should_approve:
            table_item = self.tree.focus()
            item_name = self.tree.item(table_item)["values"][0]
            approve_query = """UPDATE FarmItem
                               SET IsApproved=1
                               WHERE Name=\"{}\"""".format(item_name)
            self.db_cursor.execute(approve_query)
            self.tree.delete(table_item)
            messagebox.showinfo("Alert", "The Selected Item Has Been Approved.")
        else:
            messagebox.showinfo("Alert", "Item Not Approved.")


    def delete_button_clicked_handler(self):
        should_delete = messagebox.askyesno("Alert", "Are You Sure You Want to Delete the Selected Item?")
        if should_delete:
            table_item = self.tree.focus()
            item_name = self.tree.item(table_item)["values"][0]
            delete_query = """DELETE FROM FarmItem
                              WHERE Name=\"{}\"""".format(item_name)
            self.db_cursor.execute(delete_query)
            self.tree.delete(table_item)
            messagebox.showinfo("Alert", "The Selected Item Has Been Deleted.")
        else:
            messagebox.showinfo("Alert", "Item Not Deleted.")


    def back_button_clicked_handler(self):
        self.master.master.show_window("AdminHomeWindow")

    
    def populate_table(self):
        self.tree.delete(*self.tree.get_children())
        query = """SELECT Name, Type
                   FROM FarmItem
                   WHERE IsApproved=0"""
        self.db_cursor.execute(query)
        data = self.db_cursor.fetchall()
        for i in range(len(data)):
            row = (data[i][0], data[i][1])
            self.tree.insert("", i, values=row)
