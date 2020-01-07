#!/bin/bash
# sends a req to a URL passed as an arg and displays only the status code
curl -so /dev/null "$1" -w "%{http_code}"
