#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Merge multiple PDF files to one PDF file
Versioin 0.1: a txt file is used to store file names
"""

import datetime
import logging
import sys

from PyPDF2 import PdfMerger, PdfFileReader, PdfFileWriter

try:
    import matplotlib.pyplot as plt
except ImportError:
    logging.warn('error while importing matplotlib')


__author__ = "nonmean"
__version__ = "$Revision: 0.2 $"
__date__ = datetime.datetime.now()
__copyright__ = "Copyright (c) 2022 nonmean"
__license__ = "Python"


def merge_pdf(input_names, output_name, scale=None):
    writer = PdfFileWriter()

    for file in input_names:
        pdf = PdfFileReader(file)

        for page_number in range(0, pdf.numPages):
            page = pdf.getPage(page_number)

            if scale is not None:
                # TODO: for A4 size: float(612), float(792)
                page.scale_to(scale[0], scale[1])

            writer.addPage(page)
    
    with open(output_name, 'wb') as f:
        writer.write(f)
        f.close


def main():
    """
    pass
    """

    # TODO: handle incorrect parameters
    print(sys.argv[1:])
    
    if len(sys.argv[1:]) == 2:
        input_file, output_name = sys.argv[1:]

        try:
            input_names = open(input_file).readlines()
            
        except:
            print("something wrong while opening input file")
            return
        
        # remove the last \n if it exists
        input_names = [i[:-1] if i[-1] == "\n" else i for i in input_names]
        merge_pdf(input_names, output_name)
    
    elif len(sys.argv[1:]) == 1:
        name_string = sys.argv[1]

        input_names = []
        input_names.append("%s_Anschreiben.pdf" %name_string)
        input_names.append("%s_cv.pdf" %name_string)
        input_names.append("%s_Zertifikate.pdf" %name_string)

        output_name = ("%s_Bewerbungsunterlagen.pdf" %name_string)
        merge_pdf(input_names, output_name)

    print("Done! Yay!")


if __name__ == '__main__':
    main()
