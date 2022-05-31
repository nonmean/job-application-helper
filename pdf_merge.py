#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Merge multiple PDF files to one PDF file
Versioin 0.1: a txt file is used to store file names
"""

import datetime
import logging
import sys

from PyPDF2 import PdfMerger

try:
    import matplotlib.pyplot as plt
except ImportError:
    logging.warn('error while importing matplotlib')


__author__ = "nonmean"
__version__ = "$Revision: 0.1 $"
__date__ = datetime.datetime.now()
__copyright__ = "Copyright (c) 2022 nonmean"
__license__ = "Python"


def merge_pdf(input_names, output_name):
    merger = PdfMerger()

    for file in input_names:
        merger.append(file)

    merger.write(output_name)
    merger.close()


def main():
    """
    pass
    """

    # TODO: handle incorrect parameters
    input_file, output_name = sys.argv[1:]

    try:
        input_names = open(input_file).readlines()
        
    except:
        print("something wrong while opening input file")
        return
    
    # remove the last \n if it exists
    input_names = [i[:-1] if i[-1] == "\n" else i for i in input_names]
    merge_pdf(input_names, output_name)

    print("Done! Yay!")


if __name__ == '__main__':
    main()
