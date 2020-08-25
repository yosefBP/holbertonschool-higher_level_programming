#!/usr/bin/python3
"""
Script that takes your Github credentials (username and password) and uses
the Github API to display your id
"""


if __name__ == "__main__":
    import sys
    from requests import get, auth

    user = sys.argv[1]
    passw = sys.argv[2]
    url = 'https://api.github.com/user'
    r = get(url, auth=auth.HTTPBasicAuth(user, passw))
    try:
        js = r.json()
        print(js.get('id'))
    except ValueError:
        print("Not a valid JSON")
