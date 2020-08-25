#!/usr/bin/python3
"""
Time for an interview
"""


if __name__ == "__main__":
    import sys
    from requests import get, auth

    repository = sys.argv[1]
    user = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repository)
    r = get(url)
    try:
        js = r.json()
        for j in js[:10]:
            author, name = None, None
            sha = j.get('sha')
            commit = j.get('commit')
            if commit:
                author = commit.get('author')
            if author:
                name = author.get('name')
            print("{}: {}".format(sha, name))
    except ValueError:
        print("Not a valid JSON")
