#!/usr/bin/env python3

from send_text import send_text
from seat_checker import seat_checker
from f2l import f2l
from time import sleep

def main():  
    """Check each crn course in CRN_file and if a spot is open, send relevant
    message to provided phone_number

    CRN containing file should have the form:
    11111
    24871
    35192

    Phone number should be provided in form: 
    5555555555
    """

    #--------Insert your phone number and CRN_file name below
    phone_number="5555555555" #comment out this line if you don't want a text
    CRN_file="CRN_example.txt" #name of file
    #--------
                
    crn_list=f2l(CRN_file)

    while(True):
        message=""
        for crn in crn_list:
        	capacity, actual, remaining = seat_checker(crn)
        	if remaining>0:
        		message+="CRN "+crn+" has "+str(remaining)+" seats open"
        		print(message)
        	else:
        		print("CRN "+crn+" has no empty seats.")
        if message and phone_number: #if message is not empty and phone number supplied
            if(phone_number != "5555555555"): #make sure not using default number
                send_text(phone_number,message)

        wait_time=60*(30) #wait 30 minuts between call times
        #if wait time is too small, howdy will cut you off from too many calls
        sleep(wait_time)

if __name__=="__main__":
   main()