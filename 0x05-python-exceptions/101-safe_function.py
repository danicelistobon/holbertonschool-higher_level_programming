#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        temp = fct(*args)
        return temp
    except Exception as e:
        sys.stderr.write('Exception: {}\n'.format(e))
        return None
