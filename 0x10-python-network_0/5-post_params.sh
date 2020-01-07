#!/bin/bash
# takes in a URL, sends a POST req and displays the body of the resp
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
