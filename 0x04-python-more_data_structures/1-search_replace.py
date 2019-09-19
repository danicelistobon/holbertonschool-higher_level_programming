#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        cp_list = []
        for i in my_list:
            if i is search:
                cp_list.append(replace)
            else:
                cp_list.append(i)
        return cp_list
