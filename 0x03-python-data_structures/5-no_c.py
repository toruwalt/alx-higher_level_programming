#!/usr/bin/python3
def no_c(my_string):
    my_string_list = list(my_string)

    while "c" in my_string_list:
        my_string_list.remove("c")
    while "C" in my_string_list:
        my_string_list.remove("C")

    my_string = ''.join(my_string_list)
    return my_string
