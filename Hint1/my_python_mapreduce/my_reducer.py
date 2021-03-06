#!/usr/bin/python

# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import sys
import codecs

# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(input_stream, num_top_entries, output_stream):
    result = dict()
    for line in input_stream:
        line = line.replace("\n", "")
        item = line.split('\t')
        key = item[0]
        value = item[1]
        value = value.replace('(',"")
        value = value.replace(')',"")
        value = value.rsplit(',',1)
        subject = value[0]
        hits = int(value[1])
        if key not in result:
            result[key] = list()
        if len(result[key]) < num_top_entries:
            result[key].insert(0,(subject,hits))
        else:
            shortlist = result[key]
            swap = shortlist[0]
            for entry in shortlist:
                if entry.__getitem__(1) < swap.__getitem__(1):
                    swap = entry
            if swap.__getitem__(1) < hits:
                result[key].remove(swap)
                result[key].insert(0,(subject,hits))
    for tag in result.keys():
        for entry in result[tag]:
            output_stream.write(tag+'\t'+str(entry)+'\n')
# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(debug, i_file_name, o_file_name, num_top_entries):
    # We pick the working mode:

    # Mode 1: Debug --> We pick a file to read test the program on it
    if debug == True:
        my_input_stream = codecs.open(i_file_name, "r", encoding='utf-8')
        my_output_stream = codecs.open(o_file_name, "w", encoding='utf-8')
    # Mode 2: Actual MapReduce --> We pick std.stdin and std.stdout
    else:
        my_input_stream = sys.stdin
        my_output_stream = sys.stdout

    # We launch the Map program
    my_reduce(my_input_stream, num_top_entries, my_output_stream)

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Input parameters
    debug = True

    i_file_name = "sort_simulation.txt"
    o_file_name = "reduce_simulation.txt"

    num_top_entries = 5

    my_main(debug, i_file_name, o_file_name, num_top_entries)
