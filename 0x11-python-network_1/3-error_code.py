#!/usr/bin/python3
"""Module takes in a URL, sends a request to the URL and displays the body of
    the response (decoded in utf-8)
"""
import urllib.request
from sys import argv
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
