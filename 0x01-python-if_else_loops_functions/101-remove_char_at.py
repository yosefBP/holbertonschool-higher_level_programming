#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    length = len(str)
    count = 0
    if n <= length:
        for i in str:
            if count == n:
                count += 1
                continue
            else:
                copy += i
                count += 1
    else:
        return str
    return copy
