#!/usr/bin/env python3

from seat_checker import seat_checker
from file_to_list import file_to_list
from time import sleep


def main():
    """Check each crn course in CRN_file and if a spot is open, print a message

    CRN containing file should have the form:
    11111
    24871
    35192
    """

    # --------Insert CRN_file name below
    crn_file = "CRN_example.txt"  # name of file
    # --------

    crn_list = file_to_list(crn_file)
    year = '2018'
    semester_dict = {
        'spring': '1',
        'summer': '2',
        'fall': '3'
    }
    campus_dict = {
        'college_station': '1',
        'galveston': '2',
        'qatar': '3'
    }
    term = year + semester_dict['spring'] + campus_dict['college_station']

    while True:
        message = ""
        for crn in crn_list:
            capacity, actual, remaining = seat_checker(crn, term)
            if remaining > 0:
                message += "CRN " + crn + " has " + str(remaining) + " seats open"
                print(message)
            else:
                print("CRN " + crn + " has no empty seats.")

        wait_time = 60 * 30  # wait 30 minutes between call times
        # if wait time is too small, howdy will cut you off from too many calls
        sleep(wait_time)


if __name__ == "__main__":
    main()
