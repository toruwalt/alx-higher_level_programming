#!/usr/bin/python3
for char in reversed(range(97, 123)):
    if char % 2 != 1:
        print(chr(char))
    else:
        char -= 32
        print(chr(char))
