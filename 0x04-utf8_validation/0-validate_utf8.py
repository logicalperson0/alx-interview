#!/usr/bin/python3
"""
a module with a single function called validUTF8
"""


def validUTF8(data):
    """method that determines if a given data set represents
    a valid UTF-8 encoding"""
    # to_bytes = bytes(data)
    # print(to_bytes)
    try:
        bytes(data).decode('utf-8')
        return True
    except (UnicodeDecodeError, ValueError):
        return False
    # return True
