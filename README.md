# TAMU-Seat-Checker  
### Requirements:  
* Python 3.5.2

### Dependencies for Python3:
* requests  
* bs4 
* time

### About:
This program checks the sections you wish to register in for openings. This is done by reading the CRN's from a text file and scraping the webpage that publicly shares the number of remaining seats for your desired section. If there's an opening, a text message will be sent to your provided phone number alerting you using the TextBelt API. Upon running the program, openings will be checked for periodically (~30 minutes). This isn't done too frequently to reduce the load on your computer and the TAMU servers and ensure that you won't be disconnected. This process ends upon exiting the python program. 

### Instructions:
1. Clone this repository
2. Install Python 3.5.2 if not installed
3. Install all dependencies
  * This can be done easily by installing pip3
  * Then running "pip3 install bs4"
  * etc.
4. Create a file that lists all of the CRN's you want to check for openings as done in "CRN_example.txt"
  * Alternatively, you can just edit "CRN_example.txt and use that
5. Edit "main.py" to use your phone number and file create in Step 4
6. Run "python3  main.py"
