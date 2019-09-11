#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ch = ord(i)
        if ord(i) > 96 and ord(i) < 123:
            ch = ch - 32
        print('{}'.format(chr(ch)), end='')
    print()
