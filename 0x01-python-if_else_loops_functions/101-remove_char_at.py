#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    s = ""
    for ch in str:
        if i != n:
            s = s + ch
        i += 1
    return (s)
