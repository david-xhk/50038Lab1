#!/usr/bin/python

# Format of each line is:
# ip_address identity username time request status_code num_bytes

import sys

for line in sys.stdin:
    data = line.strip().split("\"")
    if len(data) != 3:
        continue
    before, request, after = data

    """
    data = before.strip().split(" ", 3)
    if len(data) != 4:
        continue
    ip_address, identity, username, time = data

    data = after.strip().split(" ")
    if len(data) != 2:
        continue
    status_code, num_bytes = data
    """
    
    data = request.strip().split(" ")
    if len(data) != 3:
        continue
    method, url, protocol = data
    
    data = url.rsplit("/", 1)
    if len(data) != 2:
        continue
    filePath, fileName = data
    
    if not filePath.startswith("/"):
        continue
    
    if "?" in fileName:
        fileName = fileName.split("?", 1)[0]

    if "." not in fileName:
        continue
    
    print filePath + "/" + fileName
