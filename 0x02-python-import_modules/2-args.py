#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv) - 1
    if l <= 0:
        print('{} arguments.'.format(l))
    else:
        if l == 1:
            print('{} argument:'.format(l))
        else:
            print('{} arguments:'.format(l))
    c = 1
    while c < (l + 1):
        print('{}: {}'.format(c, argv[c]))
        c = c + 1
