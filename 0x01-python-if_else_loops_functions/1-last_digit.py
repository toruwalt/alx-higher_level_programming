#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
actual_value = abs(number)
last_digit = actual_value % 10
if last_digit > 5:
    x = "and is greater than 5"
elif last_digit == 0:
    x = "and is 0"
elif last_digit <= 5:
    x = "and is less than 6 and not 0"
print(f"Last digit of {number:d} is {last_digit:d} {x}")
