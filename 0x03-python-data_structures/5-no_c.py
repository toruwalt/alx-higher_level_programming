#!/usr/bin/python3
def no_c(my_string):
    my_string_list = list(my_string)

    if 'C' in my_string:
        my_string_list.remove("C")
    elif 'c' in my_string:
        my_string_list.remove("c")

    my_string = ''.join(my_string_list)
    return my_string
