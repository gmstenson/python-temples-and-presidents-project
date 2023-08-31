import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime
import csv
from tkinter import *

PRESIDENT_INDEX = 0
BIRTHDATE_INDEX = 1
ORDINATION_INDEX = 2
DEATH_INDEX = 3
PRESIDENT_TEMPLE_ANNOUNCEMENTS_INDEX = 4
PRESIDENT_TEMPLE_GROUNDBREAKINGS_INDEX = 5
PRESIDENT_TEMPLE_DEDICATIONS_INDEX = 6
TEMPLE_NAME_INDEX = 0
TEMPLE_ANNOUNCED_INDEX = 1
TEMPLE_GROUNDBREAKING_INDEX = 2
TEMPLE_DEDICATION_INDEX = 3
TEMPLE_NUMBER_SEALING_ROOMS_INDEX = 4
TEMPLE_SQFT_INDEX = 5

def main():
    # Create the Tk root object
    root = Tk()

    Label(root, 
            text="""Please choose an option:""",
            justify = LEFT,
            font=("Times New Roman", 15),
            padx = 20).pack()

    # options for the Radiobutton and its values
    CHOICES = [("Church Presidents", "presidents"),
                ("Temples", "temples"),
                ("Temple Statistics", "statistics"),
                ("Bar Chart of Temple Statistics by Each President", "bar")]

    options = StringVar()
    options.set("presidents") #sets the radiobutton to "Church Presidents" by default
    
    # this function shows choices for the Radiobutton 
    # and calls other functions to show when chosen in the Radiobutton
    def ShowChoice():
        selection = options.get()

        if selection == "presidents":
            populate_president_window(frm_main)

        elif selection == "temples":
            populate_temple_window(frm_main)      

        elif options.get() == "statistics":
            populate_statistics_window(frm_main)

        elif options.get() == "bar":
            show_graph() 


    for choice, val in CHOICES:
        Radiobutton(root, 
                    text=choice,
                    padx = 20, 
                    font=("Times New Roman",15),
                    variable=options, 
                    command=ShowChoice,
                    value=val).pack(anchor=W)

    Label(root, 
            text="""-----------------------------------------------------------------""",
            justify = CENTER,
            font=("Times New Roman", 15),
            padx = 20).pack()


    # Main frame window
    frm_main = Frame(root)
    frm_main.master.title("Church Presidents and Temples")
    frm_main.pack(padx=5, pady=5, fill=BOTH, expand=1)

    root.mainloop()


def populate_president_window(frm_main):
    """Populate the "Church President" window of this program.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """

    lbl_name = Label(frm_main, text="Enter president:")
    ent_name = Entry(frm_main, width=25)
   
    lbl_birthdate = Label(frm_main, text="Birthdate:")
    lbl_ordination = Label(frm_main, text="Ordination:")
    lbl_death = Label(frm_main, text="Death:")
    lbl_announcements = Label(frm_main, text="Announcements:")
    lbl_groundbreakings = Label(frm_main, text="Groundbreakings:")
    lbl_dedications = Label(frm_main, text="Dedications:")
    lbl_blank2 = Label(frm_main, text="")

    lbl_dict_birthdate = Label(frm_main, width=20)
    lbl_dict_ordination = Label(frm_main, width=10)
    lbl_dict_death = Label(frm_main, width=10)
    lbl_dict_announcements = Label(frm_main, width=10)
    lbl_dict_groundbreakings = Label(frm_main, width=10)
    lbl_dict_dedications = Label(frm_main, width=4)

    lbl_3 = Label(frm_main, text="""""")

    lbl_blank = Label(frm_main, width=10)
    lbl_days_short_ag = Label(frm_main, width=10)
    lbl_days_short_gd = Label(frm_main, width=10)
    lbl_days_short_ad = Label(frm_main, width=10)
    lbl_days_long_ag = Label(frm_main, width=10)
    lbl_days_long_gd = Label(frm_main, width=10)
    lbl_days_long_ad = Label(frm_main, width=10)

    # Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_name.grid(row=0, column=0, padx=3, pady=3, ipadx=25, ipady=10)
    ent_name.grid(row=0, column=1, padx=3, pady=3, ipady=2)
    lbl_birthdate.grid(row=2, column=0, padx=3, pady=3, ipadx=20)
    lbl_dict_birthdate.grid(row=2, column=1, padx=3, pady=3, ipadx=90)
    lbl_ordination.grid(row=3, column=0, padx=3, pady=3, ipadx=20)
    lbl_dict_ordination.grid(row=3, column=1, padx=3, pady=3, ipadx=60)
    lbl_death.grid(row=4, column=0, padx=3, pady=3, ipadx=30)
    lbl_dict_death.grid(row=4, column=1, padx=3, pady=3, ipadx=60)
    lbl_announcements.grid(row=5, column=0, padx=3, pady=3, ipadx=20)
    lbl_dict_announcements.grid(row=5, column=1, padx=3, pady=3, ipadx=60)
    lbl_groundbreakings.grid(row=6, column=0, padx=3, pady=3, ipadx=20)
    lbl_dict_groundbreakings.grid(row=6, column=1, padx=3, pady=3, ipadx=60)
    lbl_dedications.grid(row=7, column=0, padx=3, pady=3, ipadx=20)
    lbl_dict_dedications.grid(row=7, column=1, padx=3, pady=3, ipadx=60)
    lbl_blank2.grid(row=8, column=0, padx=3, pady=3, ipadx=50)
    btn_clear.grid(row=8, column=1, padx=3, pady=3, ipadx=100, sticky="w")

    lbl_3.grid(row=0, column=2, padx=3, pady=3, ipadx=40)
    lbl_blank.grid(row=2, column=2, padx=3, pady=3)
    lbl_days_short_ag.grid(row=3, column=2, padx=3, pady=3)
    lbl_days_short_gd.grid(row=4, column=2, padx=3, pady=3)
    lbl_days_short_ad.grid(row=5, column=2, padx=3, pady=3)
    lbl_days_long_ag.grid(row=6, column=2, padx=3, pady=3)
    lbl_days_long_gd.grid(row=7, column=2, padx=3, pady=3)
    lbl_days_long_ad.grid(row=8, column=2, padx=3, pady=3)


    # This function will be called each time the user types 
    # the name of president correctly
    def view(event):
        
        try:
            presidents_dict = read_dict("presidents.csv", PRESIDENT_INDEX)
            name = ent_name.get()

            if name in presidents_dict:
                president_name = presidents_dict[name]
                birthdate = president_name[BIRTHDATE_INDEX]
                ordination = president_name[ORDINATION_INDEX]
                death = president_name[DEATH_INDEX]
                announcements = president_name[PRESIDENT_TEMPLE_ANNOUNCEMENTS_INDEX]
                groundbreakings = president_name[PRESIDENT_TEMPLE_GROUNDBREAKINGS_INDEX]
                dedications = president_name[PRESIDENT_TEMPLE_DEDICATIONS_INDEX]
            
                lbl_dict_birthdate.config(text=f"{birthdate}")
                lbl_dict_ordination.config(text=f"{ordination}")
                lbl_dict_death.config(text=f"{death}")
                lbl_dict_announcements.config(text=f"{announcements}")
                lbl_dict_groundbreakings.config(text=f"{groundbreakings}")
                lbl_dict_dedications.config(text=f"{dedications}")

                lbl_blank.config(text=f"")
                lbl_days_short_ag.config(text=f"")
                lbl_days_short_gd.config(text=f"")
                lbl_days_short_ad.config(text=f"")
                lbl_days_long_ag.config(text=f"")
                lbl_days_long_gd.config(text=f"")
                lbl_days_long_ad.config(text=f"")

        except ValueError:
            lbl_dict_birthdate.config(text="")
            lbl_dict_ordination.config(text="")
            lbl_dict_death.config(text="")
            lbl_dict_announcements.config(text="")
            lbl_dict_groundbreakings.config(text="")
            lbl_dict_dedications.config(text="")

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_name.delete(0, END)
        # lbl_dict_president.config(text="")
        lbl_dict_birthdate.config(text="")
        lbl_dict_ordination.config(text="")
        lbl_dict_death.config(text="")
        lbl_dict_announcements.config(text="")
        lbl_dict_groundbreakings.config(text="")
        lbl_dict_dedications.config(text="")
        ent_name.focus()

    ent_name.bind("<KeyRelease>", view)
    btn_clear.config(command=clear)
    ent_name.focus()


def populate_temple_window(frm_main):
    """Populate the "Temples" window of this program. 

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """

    lbl_name = Label(frm_main, text="Enter temple:")
    ent_name = Entry(frm_main, width=25)
   
    lbl_temple = Label(frm_main, text="Temple:")
    lbl_announced = Label(frm_main, text="Announced:")
    lbl_groundbreaking = Label(frm_main, text="Groundbreaking:")
    lbl_dedication = Label(frm_main, text="Dedication:")
    lbl_sealing_rooms = Label(frm_main, text="Sealing Rooms:")
    lbl_sqft = Label(frm_main, text="Square Footage:")
    lbl_blank2 = Label(frm_main, text="")

    lbl_dict_temple = Label(frm_main, width=20)
    lbl_dict_announced = Label(frm_main, width=10)
    lbl_dict_groundbreaking = Label(frm_main, width=10)
    lbl_dict_dedication = Label(frm_main, width=10)
    lbl_dict_sealing_rooms = Label(frm_main, width=10)
    lbl_dict_sqft = Label(frm_main, width=10)

    lbl_3 = Label(frm_main, text="""""")

    lbl_blank = Label(frm_main, width=10)
    lbl_days_short_ag = Label(frm_main, width=10)
    lbl_days_short_gd = Label(frm_main, width=10)
    lbl_days_short_ad = Label(frm_main, width=10)
    lbl_days_long_ag = Label(frm_main, width=10)
    lbl_days_long_gd = Label(frm_main, width=10)
    lbl_days_long_ad = Label(frm_main, width=10)

    # Clear button
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_name.grid(row=0, column=0, padx=3, pady=3, ipadx=25, ipady=10)
    ent_name.grid(row=0, column=1, padx=3, pady=3, ipady=2)
    lbl_temple.grid(row=2, column=0, padx=3, pady=3, ipadx=20)
    lbl_dict_temple.grid(row=2, column=1, padx=3, pady=3, ipadx=90)
    lbl_announced.grid(row=3, column=0, padx=3, pady=3, ipadx=20)
    lbl_dict_announced.grid(row=3, column=1, padx=3, pady=3, ipadx=60)
    lbl_groundbreaking.grid(row=4, column=0, padx=3, pady=3, ipadx=20)
    lbl_dict_groundbreaking.grid(row=4, column=1, padx=3, pady=3, ipadx=60)
    lbl_dedication.grid(row=5, column=0, padx=3, pady=3, ipadx=20)
    lbl_dict_dedication.grid(row=5, column=1, padx=3, pady=3, ipadx=60)
    lbl_sealing_rooms.grid(row=6, column=0, padx=3, pady=3, ipadx=20)
    lbl_dict_sealing_rooms.grid(row=6, column=1, padx=3, pady=3, ipadx=60)
    lbl_sqft.grid(row=7, column=0, padx=3, pady=3, ipadx=20)
    lbl_dict_sqft.grid(row=7, column=1, padx=3, pady=3, ipadx=60)
    lbl_blank2.grid(row=8, column=0, padx=3, pady=3, ipadx=50)
    btn_clear.grid(row=8, column=1, padx=3, pady=3, ipadx=100, sticky="w")

    lbl_3.grid(row=0, column=2, padx=3, pady=3, ipadx=40)
    lbl_blank.grid(row=2, column=2, padx=3, pady=3)
    lbl_days_short_ag.grid(row=3, column=2, padx=3, pady=3)
    lbl_days_short_gd.grid(row=4, column=2, padx=3, pady=3)
    lbl_days_short_ad.grid(row=5, column=2, padx=3, pady=3)
    lbl_days_long_ag.grid(row=6, column=2, padx=3, pady=3)
    lbl_days_long_gd.grid(row=7, column=2, padx=3, pady=3)
    lbl_days_long_ad.grid(row=8, column=2, padx=3, pady=3)


    # This function will be called each time the user types
    # the name of the temple correctly
    def view(event):
        
        try:
            temples_dict = read_dict("temples.csv", TEMPLE_NAME_INDEX)
            temple = ent_name.get()

            if temple in temples_dict:
                temple_name = temples_dict[temple]
                temple_full_name = temple_name[TEMPLE_NAME_INDEX]
                announced = temple_name[TEMPLE_ANNOUNCED_INDEX]
                groundbreaking = temple_name[TEMPLE_GROUNDBREAKING_INDEX]
                dedication = temple_name[TEMPLE_DEDICATION_INDEX]
                sealing_rooms = temple_name[TEMPLE_NUMBER_SEALING_ROOMS_INDEX]
                sqft = temple_name[TEMPLE_SQFT_INDEX]
            
                lbl_dict_temple.config(text=f"{temple_full_name}")
                lbl_dict_announced.config(text=f"{announced}")
                lbl_dict_groundbreaking.config(text=f"{groundbreaking}")
                lbl_dict_dedication.config(text=f"{dedication}")
                lbl_dict_sealing_rooms.config(text=f"{sealing_rooms}")
                lbl_dict_sqft.config(text=f"{sqft} sqft")

                lbl_blank.config(text=f"")
                lbl_days_short_ag.config(text=f"")
                lbl_days_short_gd.config(text=f"")
                lbl_days_short_ad.config(text=f"")
                lbl_days_long_ag.config(text=f"")
                lbl_days_long_gd.config(text=f"")
                lbl_days_long_ad.config(text=f"")

        except ValueError:
            lbl_dict_temple.config(text="")
            lbl_dict_announced.config(text="")
            lbl_dict_groundbreaking.config(text="")
            lbl_dict_dedication.config(text="")
            lbl_dict_sealing_rooms.config(text="")
            lbl_dict_sqft.config(text="")

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_name.delete(0, END)
        lbl_dict_temple.config(text="")
        lbl_dict_announced.config(text="")
        lbl_dict_groundbreaking.config(text="")
        lbl_dict_dedication.config(text="")
        lbl_dict_sealing_rooms.config(text="")
        lbl_dict_sqft.config(text="")
        ent_name.focus()

    ent_name.bind("<KeyRelease>", view)
    btn_clear.config(command=clear)
    ent_name.focus()

    
def populate_statistics_window(frm_main):
    """Populate the "Statistics" window of this program. 

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """

    lbl_1 = Label(frm_main, 
            text="""A-Announcement\nG-Groundbreaking\nD-Dedication""",
            justify = LEFT,
            font=("Times New Roman", 8))
    lbl_2 = Label(frm_main, 
            text="""Temple Name""",
            justify = LEFT,
            font=("Times New Roman", 15))
    lbl_3 = Label(frm_main, 
            text="""Duration""",
            justify = LEFT,
            font=("Times New Roman", 15))
   
    lbl_oldest = Label(frm_main, text="Oldest Temple:")
    lbl_long_ag = Label(frm_main, text="Longest A to G:")
    lbl_long_gd = Label(frm_main, text="Longest G to D:")
    lbl_long_ad = Label(frm_main, text="Longest A to D:")
    lbl_short_ag = Label(frm_main, text="Shortest A to G:")
    lbl_short_gd = Label(frm_main, text="Shortest G to D:")
    lbl_short_ad = Label(frm_main, text="Shortest A to D:")

    lbl_dict_oldest_temple = Label(frm_main, width=20)
    lbl_dict_short_ag = Label(frm_main, width=30)
    lbl_dict_short_gd = Label(frm_main, width=20)
    lbl_dict_short_ad = Label(frm_main, width=20)
    lbl_dict_long_ag = Label(frm_main, width=20)
    lbl_dict_long_gd = Label(frm_main, width=20)
    lbl_dict_long_ad = Label(frm_main, width=20)

    lbl_days_oldest_temple = Label(frm_main, width=10)
    lbl_days_short_ag = Label(frm_main, width=10)
    lbl_days_short_gd = Label(frm_main, width=10)
    lbl_days_short_ad = Label(frm_main, width=10)
    lbl_days_long_ag = Label(frm_main, width=10)
    lbl_days_long_gd = Label(frm_main, width=10)
    lbl_days_long_ad = Label(frm_main, width=10)

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_1.grid(row=0, column=0, padx=3, pady=3, ipadx=20)
    lbl_oldest.grid(row=2, column=0, padx=3, pady=3, ipadx=10)
    lbl_long_ag.grid(row=3, column=0, padx=3, pady=3, ipadx=10)
    lbl_long_gd.grid(row=4, column=0, padx=3, pady=3, ipadx=10)
    lbl_long_ad.grid(row=5, column=0, padx=3, pady=3, ipadx=10)
    lbl_short_ag.grid(row=6, column=0, padx=3, pady=3, ipadx=10)
    lbl_short_gd.grid(row=7, column=0, padx=3, pady=3, ipadx=10)
    lbl_short_ad.grid(row=8, column=0, padx=3, pady=3, ipadx=10)

    lbl_2.grid(row=0, column=1, padx=3, pady=3, ipadx=80, ipady=10)
    lbl_dict_oldest_temple.grid(row=2, column=1, padx=3, pady=3, ipadx=80)
    lbl_dict_short_ag.grid(row=3, column=1, padx=3, pady=3)
    lbl_dict_short_gd.grid(row=4, column=1, padx=3, pady=3)
    lbl_dict_short_ad.grid(row=5, column=1, padx=3, pady=3)
    lbl_dict_long_ag.grid(row=6, column=1, padx=3, pady=3)
    lbl_dict_long_gd.grid(row=7, column=1, padx=3, pady=3)
    lbl_dict_long_ad.grid(row=8, column=1, padx=3, pady=3, ipadx=100, ipady=3)

    lbl_3.grid(row=0, column=2, padx=3, pady=3, ipadx=20)
    lbl_days_oldest_temple.grid(row=2, column=2, padx=3, pady=3)
    lbl_days_short_ag.grid(row=3, column=2, padx=3, pady=3)
    lbl_days_short_gd.grid(row=4, column=2, padx=3, pady=3)
    lbl_days_short_ad.grid(row=5, column=2, padx=3, pady=3)
    lbl_days_long_ag.grid(row=6, column=2, padx=3, pady=3)
    lbl_days_long_gd.grid(row=7, column=2, padx=3, pady=3)
    lbl_days_long_ad.grid(row=8, column=2, padx=3, pady=3)
    
    # get the current date with the same format in the csv file
    current_date = datetime.now().strftime("%d-%b-%Y")
    temples_dict = read_dict("temples.csv", TEMPLE_NAME_INDEX)

    gb_max_days = -1
    de_max_days = -1
    ade_max_days = -1
    max_days = -1
    gb_min_days = 99999999
    de_min_days = 99999999
    ade_min_days = 99999999
    old_temp_name = ""
    gb_max_temp_name = ""
    de_max_temp_name = ""
    ade_max_temp_name = ""
    gb_min_temp_name = ""
    de_min_temp_name = ""
    ade_min_temp_name = ""

    for temple in temples_dict:
        temple_name = temples_dict[temple]
        temple_full_name = temple_name[TEMPLE_NAME_INDEX]
        announced = temple_name[TEMPLE_ANNOUNCED_INDEX]
        groundbreaking = temple_name[TEMPLE_GROUNDBREAKING_INDEX]
        dedication = temple_name[TEMPLE_DEDICATION_INDEX]

        oldest_temple = days_between(current_date, dedication)
        announcement_to_groundbreaking = days_between(announced, groundbreaking)
        groundbreaking_to_dedication = days_between(groundbreaking, dedication)
        announcement_to_dedication = days_between(announced, dedication)

        # this gets the the highest and lowest difference between two dates
        # as well as its corresponding temple
        if oldest_temple > max_days:
            max_days = oldest_temple
            old_temp_name = temple_full_name

        if announcement_to_groundbreaking > gb_max_days:
            gb_max_days = announcement_to_groundbreaking
            gb_max_temp_name = temple_full_name

        if groundbreaking_to_dedication > de_max_days:
            de_max_days = groundbreaking_to_dedication
            de_max_temp_name = temple_full_name

        if announcement_to_dedication > ade_max_days:
            ade_max_days = announcement_to_dedication
            ade_max_temp_name = temple_full_name

        if announcement_to_groundbreaking < gb_min_days:
            gb_min_days = announcement_to_groundbreaking
            gb_min_temp_name = temple_full_name

        if groundbreaking_to_dedication < de_min_days:
            de_min_days = groundbreaking_to_dedication
            de_min_temp_name = temple_full_name

        if announcement_to_dedication < ade_min_days:
            ade_min_days = announcement_to_dedication
            ade_min_temp_name = temple_full_name
    
    lbl_dict_oldest_temple.config(text=f"{old_temp_name}")
    lbl_dict_short_ag.config(text=f"{gb_max_temp_name}")
    lbl_dict_short_gd.config(text=f"{de_max_temp_name}")
    lbl_dict_short_ad.config(text=f"{ade_max_temp_name}")
    lbl_dict_long_ag.config(text=f"{gb_min_temp_name}")
    lbl_dict_long_gd.config(text=f"{de_min_temp_name}")
    lbl_dict_long_ad.config(text=f"{ade_min_temp_name}")

    lbl_days_oldest_temple.config(text=f"{max_days} days")
    lbl_days_short_ag.config(text=f"{gb_max_days} days")
    lbl_days_short_gd.config(text=f"{de_max_days} days")
    lbl_days_short_ad.config(text=f"{ade_max_days} days")
    lbl_days_long_ag.config(text=f"{gb_min_days} days")
    lbl_days_long_gd.config(text=f"{de_min_days} days")
    lbl_days_long_ad.config(text=f"{ade_min_days} days")


# this function subtracts two given dates and returns number of days
def days_between(date1, date2):
    date1 = datetime.strptime(date1, "%d-%b-%Y")
    date2 = datetime.strptime(date2, "%d-%b-%Y")

    return abs((date2-date1).days)

# this function reads the csv file using pandas and 
# creates a bar graph using matplotlib with the data from the csv file
def show_graph():
    
    plt.style.use('fivethirtyeight')
    fig = plt.gcf()
    fig.canvas.manager.set_window_title("Bar Chart")
    fig.subplots_adjust(bottom=0.25)

    # read the csv file using pandas and store it in the variable 'temples'
    temples = pd.read_csv("presidents.csv")

    # this gets the entities from the csv file 
    # that will be used in the bar chart
    # x axis: presidents 
    # y axis: number of groundbreakings, dedications, and announcements
    presidents = temples.President
    groundbreakings = temples.Groundbreakings
    dedications = temples.Dedications
    announcements = temples.Announcements

    x_indexes = np.arange(len(presidents))
    w = 0.25

    # setting the 'w' allows to show multiple bar charts
    plt.bar(x_indexes - w, announcements, width = w, color = '#28536B', label='Announcements')
    plt.bar(x_indexes, groundbreakings, width = w, color = '#4F3130', label='Groundbreakings')
    plt.bar(x_indexes + w, dedications, width = w, color = '#6BA368', label='Dedications')

    # this puts title in the chart, labels for x and y axis, legends,
    # and label font sizes
    title_string = "Temple Statistics per President"
    subtitle_string = "**Data as of April 2022**"

    plt.suptitle(title_string, fontsize=12)
    plt.title(subtitle_string, fontsize=8)
    plt.xlabel("Church Presidents", fontsize=10)
    plt.ylabel("Number of Temples", fontsize=10)
    plt.tick_params(axis='x', which='major', labelsize=6)
    plt.tick_params(axis='y', which='major', labelsize=8)
    plt.xticks(x_indexes, presidents, rotation = 90)
    plt.legend(loc=2, prop={'size': 10})

    plt.show()


# this function reads the csv file and returns a dictionary
def read_dict(filename, key_column_index):
    
    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list

    return dictionary


if __name__ == "__main__":
    main()