#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for string in dir(hidden_4):
        if string[0] != '_' and string[1] != '_':
            print(string)
