#!/usr/bin/env python3

from send_text import send_text
from seat_checker import seat_checker
from f2l import f2l
import sys

def main(CRN_file, phone_number):  
    """Check each crn course in CRN_file and if a spot is open, send relevant
    message to provided phone_number

    CRN containing file should have the form:
    11111
    24871
    35192

    Phone number should be provided in form: 
    5555555555
    """
    if(len(phone_number) != 10):
        print("Improper format for phone number. Use form: 555555555")
        print("No text message will be sent\n")
                
    crn_list=f2l(CRN_file)
    message=""
    for crn in crn_list[:]:
    	capacity, actual, remaining = seat_checker(crn)
    	if remaining>0:
    		message+="CRN "+crn+" has "+str(remaining)+" seats open"
    		print(message)
    	else:
    		print("CRN "+crn+" has no empty seats.")
    if message and phone_number: #if message is not empty and phone number supplied
     	send_text(phone_number,message)

if __name__=="__main__":
   main()