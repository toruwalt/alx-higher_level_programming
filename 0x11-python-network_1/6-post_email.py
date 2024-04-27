#!/usr/bin/python3
"""Script that takes in a URL and an email address, 
    sends a POST request to the URL with email
    use requests and sys
"""

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    value = {
            'email' : sys.argv[2]
            }

    r = requests.post(url, data=value)
    print(r.text)
    
