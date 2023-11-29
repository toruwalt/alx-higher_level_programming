#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_digit = number % 10
    else:
        x = -(number)
        last_digit = x % 10
    print("{}".format(last_digit), end="")
    return last_digit
