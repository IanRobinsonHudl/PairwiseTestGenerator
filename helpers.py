#!/usr/bin/env python
# -*- coding: utf-8 -*-


# method prepares rows in constraint file for use in is_valid_combination method
# get index and item values for each constraint and store as a list,
# then store each list as a set of nested lists for use in is_valid_row method,
def get_constraints(constraints):
    all_con_lists = []
    for row in constraints:
        con_list = []
        for index, item in enumerate(row):
            if item != "":
                con_list.append(int(index))
                con_list.append(item)
        all_con_lists.append(con_list)
    return all_con_lists


# define method to strip out unwanted characters from created pairwise set
def stringclean(dirtystring):
    dirtystring = dirtystring.replace(", ", ",")
    dirtystring = dirtystring.replace("'", "")
    dirtystring = dirtystring.replace("\\n", "")
    dirtystring = dirtystring.replace("[", "")
    cleanstring = dirtystring.replace("]", "")
    return cleanstring + "\n"
