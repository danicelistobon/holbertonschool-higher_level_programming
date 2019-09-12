#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    l = len(argv)
    r = 0
    if l != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            r = add(a, b)
            print('{:d} + {:d} = {:d}'.format(a, b, r))
        elif argv[2] == '-':
            r = sub(a, b)
            print('{:d} - {:d} = {:d}'.format(a, b, r))
        elif argv[2] == '*':
            r = mul(a, b)
            print('{:d} * {:d} = {:d}'.format(a, b, r))
        elif argv[2] == '/':
            r = div(a, b)
            print('{:d} / {:d} = {:d}'.format(a, b, r))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
