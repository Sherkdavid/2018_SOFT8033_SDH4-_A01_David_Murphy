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
import csv

# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def my_map(input_stream, languages, num_top_entries, output_stream):
    #tokenize for readability
    reader = csv.reader(input_stream,delimiter=' ')
    #dictionary to store result keys
    result = dict()
    for row in reader:
        #split tag to detect language
        hits = int(row[2])
        subject = row[1]
        tag = row[0].split('.')
        if tag[0] in languages:
            #if tag isn't listed add it
            if not result.keys().__contains__(row[0]):
                result[row[0]] = list()
                result[row[0]].insert(0,(subject,hits))
            else:
                candidates = result[row[0]]
                if len(candidates) < num_top_entries:
                    candidates.insert(0,(subject,hits))
                else:
                    swap = candidates[0]
                    for candidate in candidates:
                        if candidate[1] < swap[1]:
                            swap = candidate
                    if swap[1] < hits:
                        candidates.remove(swap)
                        candidates.insert(0,(subject,hits))
    for key in result.keys():
        for candidate in result[key]:
            output_stream.write(key+"\t"+str(candidate)+"\n")
# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(debug, i_file_name, o_file_name, languages, num_top_entries):
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
    my_map(my_input_stream, languages, num_top_entries, my_output_stream)

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Input parameters
    debug = False

    i_file_name = "pageviews-20180219-100000_0.txt"
    o_file_name = "mapResult.txt"

    languages = ["en", "es", "fr"]
    num_top_entries = 5

    # 2. Call to the function
    my_main(debug, i_file_name, o_file_name, languages, num_top_entries)
