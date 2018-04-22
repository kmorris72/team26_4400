#NOTES:
#Stuff to do:
#1. Add the pass in of the property name

from tkinter import *
import tkinter.messagebox as messagebox
import MySQLdb as sql

#db = sql.connect(host="academic-mysql.cc.gatech.edu",
#                user="cs4400_team_26", passwd="YFxUWSqD",
#                db="cs4400_team_26")

#root = Tk()

class PropertyDetailsWindow(Frame):
    def __init__(self, parent, db_cursor):
        Frame.__init__(self, parent)
        self.db_cursor = db_cursor
        #self.master = master
        #master.title(current_property + " Property Details")

        current_property = "Jacob's Farm"
        
        prop_detail_query = "SELECT * FROM Property WHERE Name=\"{}\"".format(current_property)
        self.db_cursor.execute(prop_detail_query)
        prop_details = self.db_cursor.fetchall()
        #print(prop_details[0])
        prop_id = prop_details[0][0]
        prop_size = prop_details[0][2]
        prop_commercial = prop_details[0][3]
        prop_public = prop_details[0][4]
        prop_address = prop_details[0][5]
        prop_city = prop_details[0][6]
        prop_zip = prop_details[0][7]
        prop_type = prop_details[0][8]
        prop_owner = prop_details[0][9]
        if prop_commercial == 1:
            prop_commercial = "Yes"
        else: 
            prop_commercial = "No"
        if prop_public == 1:
            prop_public = "Yes"
        else:
            prop_public = "No"
        prop_type = (prop_type[0].upper() + prop_type[1:].lower())
        prop_id = str(prop_id).zfill(5)
        email_query = "SELECT Email FROM User WHERE Username=\"{}\"".format(prop_owner)
        self.db_cursor.execute(email_query)
        prop_owner_email = self.db_cursor.fetchall()[0][0]

        visits_query = "SELECT COUNT(PropertyID) FROM Visit WHERE PropertyID =\"{}\"".format(prop_id)
        self.db_cursor.execute(visits_query)
        prop_visits = self.db_cursor.fetchall()[0][0]

        avg_rating_query = "SELECT AVG(Rating) FROM Visit WHERE PropertyID =\"{}\"".format(prop_id)
        self.db_cursor.execute(visits_query)
        prop_avg_rtg = self.db_cursor.fetchall()[0][0]
        if prop_visits == 0:
            prop_avg_rtg = "No Visits Yet"

        crops_query = "SELECT ItemName FROM Has LEFT OUTER JOIN FarmItem ON Has.ItemName=FarmItem.Name WHERE PropertyID =\"{}\" and Type !=\"ANIMAL\"".format(prop_id)
        self.db_cursor.execute(crops_query)
        prop_crops = self.db_cursor.fetchall()
        prop_crop_list = ""
        for item in prop_crops:
            prop_crop_list = prop_crop_list + item[0] + ", "
        prop_crop_list = prop_crop_list[0:len(prop_crop_list)-2]

        animal_query = "SELECT ItemName FROM Has LEFT OUTER JOIN FarmItem ON Has.ItemName=FarmItem.Name WHERE PropertyID =\"{}\" and Type =\"ANIMAL\"".format(prop_id)
        self.db_cursor.execute(animal_query)
        prop_animals = self.db_cursor.fetchall()
        prop_animal_list = ""
        for item in prop_animals:
            prop_animal_list = prop_animal_list + item[0] + ", "
        prop_animal_list = prop_animal_list[0:len(prop_animal_list)-2]


        Label(self, text=current_property + " Property Details", font="Times 24"). grid(row=0, columnspan=6)

        Label(self, text="Name:", font="Times 12").grid(row=1,column=0, sticky=E, padx=0)
        Label(self, text=current_property, font="Times 12").grid(row=1,column=1, sticky=W, padx=0)

        Label(self, text="Owner:", font="Times 12").grid(row=2,column=0, sticky=E, padx=0)
        Label(self, text=prop_owner, font="Times 12").grid(row=2,column=1, sticky=W, padx=0)

        Label(self, text="Owner Email:", font="Times 12").grid(row=3,column=0, sticky=E, padx=0)
        Label(self, text=prop_owner_email, font="Times 12").grid(row=3,column=1, sticky=W, padx=0)

        Label(self, text="Visits:", font="Times 12").grid(row=4,column=0, sticky=E, padx=0)
        Label(self, text=prop_visits, font="Times 12").grid(row=4,column=1, sticky=W, padx=0)

        Label(self, text="Address:", font="Times 12").grid(row=5,column=0, sticky=E, padx=0)
        Label(self, text=prop_address, font="Times 12").grid(row=5,column=1, sticky=W, padx=0)

        Label(self, text="City:", font="Times 12").grid(row=6,column=0, sticky=E, padx=0)
        Label(self, text=prop_city, font="Times 12").grid(row=6,column=1, sticky=W, padx=0)

        Label(self, text="Zip:", font="Times 12").grid(row=7,column=0, sticky=E, padx=0)
        Label(self, text=prop_zip, font="Times 12").grid(row=7,column=1, sticky=W, padx=0)

        Label(self, text="Size (Acres):", font="Times 12").grid(row=8,column=0, sticky=E, padx=0)
        Label(self, text=prop_size, font="Times 12").grid(row=8,column=1, sticky=W, padx=0)

        Label(self, text="Avg Rating:", font="Times 12").grid(row=9,column=0, sticky=E, padx=0)
        Label(self, text=prop_avg_rtg, font="Times 12").grid(row=9,column=1, sticky=W, padx=0)

        Label(self, text="Type:", font="Times 12").grid(row=10,column=0, sticky=E, padx=0)
        Label(self, text=prop_type, font="Times 12").grid(row=10,column=1, sticky=W, padx=0)

        Label(self, text="Public:", font="Times 12").grid(row=11,column=0, sticky=E, padx=0)
        Label(self, text=prop_public, font="Times 12").grid(row=11,column=1, sticky=W, padx=0)

        Label(self, text="Commercial:", font="Times 12").grid(row=12,column=0, sticky=E, padx=0)
        Label(self, text=prop_commercial, font="Times 12").grid(row=12,column=1, sticky=W, padx=0)

        Label(self, text="ID:", font="Times 12").grid(row=13,column=0, sticky=E, padx=0)
        Label(self, text=prop_id, font="Times 12").grid(row=13,column=1, sticky=W, padx=0)

        Label(self, text="Crops:", font="Times 12").grid(row=14,column=0, sticky=E, padx=0)
        Label(self, text=prop_crop_list, font="Times 12").grid(row=14,column=1, sticky=W, padx=0)

        Label(self, text="Animals:", font="Times 12").grid(row=15,column=0, sticky=E, padx=0)
        Label(self, text=prop_animal_list, font="Times 12").grid(row=15,column=1, sticky=W, padx=0)

        self.backButton = Button(self, text="Back",
                                command=self.back_event_handler)
        self.backButton.grid(row=16,column=0, sticky=W+E,columnspan=2)

    def back_event_handler(self):
        self.master.master.show_window("OwnerViewOtherOwnersPropertiesWindow")
