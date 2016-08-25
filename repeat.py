#!/usr/bin/env python3

from random import random
from time import sleep
import sys
from main import main

def repeat(argv):
    CRN_file=first_argument=argv[1]
    phone_number=second_argument=argv[2]
    while(True):
        main(CRN_file,phone_number)
        wait_time=60*(30) #wait 30 minuts between call times
        #if wait time is too small, howdy will cut you off from too many calls
        sleep(wait_time)

if __name__=="__main__":
   repeat(sys.argv)