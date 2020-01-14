#!/usr/bin/python3
"""Module that  that takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8)
"""
import urllib.request
from sys import argv
import urllib.parse


if __name__ == "__main__":
    data_req = urllib.parse.urlencode({'email': argv[2]}).encode('ascii')
    with urllib.request.urlopen(url=argv[1], data=data_req) as response:
        print(response.read().decode('utf8'))
