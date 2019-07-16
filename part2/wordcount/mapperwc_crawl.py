#!/usr/bin/env python

"""mapper.py"""

import sys

stop_words=["african","work","woman", "student","series", "workshop", "event", "engine"]
# input comes from STDIN (standard input)
for line in sys.stdin:
    # change the text to lowercase
    line = line.lower()
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()

    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if not (word[0].isdigit()) and word not in stop_words:
            print ('%s\t%s' % (word, 1))