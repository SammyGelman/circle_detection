#!/usr/bin/env python3
import os

def gen_neg_description_file():
    # open the output file for writing. This will delete all existing data for
    # that address
    with open('neg.txt', 'w') as f:
        # loop over all filenames
        for filename in os.listdir('negatives'):
            f.write('negatives/' + filename + '\n')

gen_neg_description_file()
