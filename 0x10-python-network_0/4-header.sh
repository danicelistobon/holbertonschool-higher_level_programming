#!/bin/bash
# takes in a URL as an arg, sends a GET req and displays the body of the resp
curl -sH "X-HolbertonSchool-User-Id:98" "$1"
