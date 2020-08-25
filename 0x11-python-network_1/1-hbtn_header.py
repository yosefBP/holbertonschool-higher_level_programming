#!/usr/bin/python3
"""
 Script that takes in a URL, sends a request to the URL and displays the
 value of the X-Request-Id
"""


if __name__ == "__main__":
    import urllib.request
    import sys
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            Xreq = response.info().get('X-Request-Id')
            print(Xreq)
    except:
        pass
