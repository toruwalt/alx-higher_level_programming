#!/usr/bin/python3
def islower(c):
    if ord(c) > 96:
        if ord(c) < 122:
            return True
        else:
            return False
