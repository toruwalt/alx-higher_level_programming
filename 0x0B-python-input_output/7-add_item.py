#!/usr/bin/python3
"""A script that adds all arguments to a Python list, and then save them to a file"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    load_from_json_file("add_item.json")
except Exception:
    m = list()
    for x in sys.argv[1:]:
        m.append(x)
    print(m)

save_to_json_file(m, "add_item.json")
load_from_json_file("add_item.json")
