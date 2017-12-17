#!/usr/bin/env python3

import requests
from lxml import html


def seat_checker(crn, term):
    """Check capacity, actual, and remaining seats for crn course"""

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
    url = "https://compass-ssb.tamu.edu/pls/PROD/bwykschd.p_disp_detail_sched"
    payload = {'term_in': term, 'crn_in': crn}
    page = requests.get(url, headers=headers, params=payload)
    tree = html.fromstring(page.content)
    capacity = int(tree.xpath('/html/body/div[3]/table[1]/tr[2]/td/table/tr[2]/td[1]/text()')[0])
    actual = int(tree.xpath('/html/body/div[3]/table[1]/tr[2]/td/table/tr[2]/td[2]/text()')[0])
    remaining = int(tree.xpath('/html/body/div[3]/table[1]/tr[2]/td/table/tr[2]/td[3]/text()')[0])
    return capacity, actual, remaining
