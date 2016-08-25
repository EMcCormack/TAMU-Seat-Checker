#!/usr/bin/env python3

#https://www.reddit.com/r/Python/comments/2m8ved/textbelt_send_sms_with_no_signup/cm28xx0

import requests

def send_text(phone_number, message):
    """Send message to phone_number using textbelt API"""
    message = {"number": phone_number, "message": message}
    r = requests.post("http://textbelt.com/text", data=message)
    return r.status_code, r.text