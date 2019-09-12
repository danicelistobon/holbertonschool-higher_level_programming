#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    c = 1
    suma = 0
    while c < len(argv):
        suma = suma + int(argv[c])
        c = c + 1
    print('{}'.format(suma))
