#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def seat_checker(crn):
	"""Check capacity, actual, and remaining seats for crn course"""

	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}

	url = "https://compass-ssb.tamu.edu/pls/PROD/bwykschd.p_disp_detail_sched"
	payload = {'term_in': '201631', 'crn_in': crn}
	seats=[]
	response = requests.get(url, headers=headers, params=payload)
	body = response.content
	soup = BeautifulSoup(body,'lxml')
	for div in soup.find_all('div', attrs={'class':'pagebodydiv'}):
		for table in div.find_all('table',attrs={'class':'datadisplaytable'}):
			for sub_table in table.find_all('table',attrs={'class':'datadisplaytable'}):
				for td in sub_table.find_all('td',attrs={'class':'dddefault'}):
					info=td.renderContents().decode("utf-8")
					seats.append(info)
	capacity = int(seats[0])
	actual = int(seats[1])
	remaining = int(seats[2])
	return capacity, actual, remaining