#!/usr/bin/python3
"""Script that takes in a URL and an email"""
import sys
import requests


if __name__ == '__main__':
#    try:
        letter = sys.argv[1]
        lll = {'q':letter}
        url = 'http://0.0.0.0:5000/search_user'
        r = requests.post(url, data=lll)
        m = r.json()
        print("[{}] {}".format(m["id"], m["name"]))
