#!/usr/bin/python

# Format of each line is:
# ip_address identity username time request status_code num_bytes

import sys

for line in sys.stdin:
    data = line.strip().split("\"")
    if len(data) != 3:
        continue
    before, request, after = data

    data = before.strip().split(" ", 3)
    if len(data) != 4:
        continue
    ip_address, identity, username, time = data    
    
    data = request.strip().split(" ")
    if len(data) != 3:
        continue
    method, url, protocol = data
    
    if url.startswith("/"):
        print ip_address
