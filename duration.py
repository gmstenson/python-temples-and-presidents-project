from argparse import _MutuallyExclusiveGroup
from datetime import datetime, timedelta, date
import csv

TEMPLE_NAME_INDEX = 0
TEMPLE_ANNOUNCED_INDEX = 1
TEMPLE_GROUNDBREAKING_INDEX = 2
TEMPLE_DEDICATION_INDEX = 3
TEMPLE_NUMBER_SEALING_ROOMS_INDEX = 4
TEMPLE_SQFT_INDEX = 5

def main():

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

        # announced_date = datetime.strptime(announced_date, "%d-%b-%Y")
        # groundbreaking_date = datetime.strptime(groundbreaking_date, "%d-%b-%Y")
        # dedication_date = datetime.strptime(dedication_date, "%d-%b-%Y")

        oldest_temple = days_between(current_date, dedication)
        announcement_to_groundbreaking = days_between(announced, groundbreaking)
        groundbreaking_to_dedication = days_between(groundbreaking, dedication)
        announcement_to_dedication = days_between(announced, dedication)

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



    print(f"Oldest Operating Temple: {old_temp_name} - {max_days}")
    print(f"Longest Announcement to Groundbreaking: {gb_max_temp_name} - {gb_max_days}")
    print(f"Longest Groundbreaking to Dedication: {de_max_temp_name} - {de_max_days}")
    print(f"Longest Announcement to Dedication: {ade_max_temp_name} - {ade_max_days}")
    print(f"Shortest Announcement to Groundbreaking: {gb_min_temp_name} - {gb_min_days}")
    print(f"Shortest Groundbreaking to Dedication: {de_min_temp_name} - {de_min_days}")
    print(f"Shortest Announcement to Dedication: {ade_min_temp_name} - {ade_min_days}")





def days_between(date1, date2):
    date1 = datetime.strptime(date1, "%d-%b-%Y")
    date2 = datetime.strptime(date2, "%d-%b-%Y")

    return abs((date2-date1).days)



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