#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Merge multiple figures to one PDF file
Versioin 0.1: a txt file is used to store file names
"""

import datetime
import sys

from PIL import Image


__author__ = "nonmean"
__version__ = "$Revision: 0.1 $"
__date__ = datetime.datetime.now()
__copyright__ = "Copyright (c) 2022 nonmean"
__license__ = "Python"


def save_pdf(file_name, img_names):
    imgs = [Image.open(i).convert("RGB") for i in img_names]

    if len(imgs) == 1:
        imgs[0].save(file_name, save_all=True)
    else:
        imgs[0].save(file_name, save_all=True, append_images=imgs[1:])


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

        save_pdf(output_name, input_names)

    print("Done! Yay!")


if __name__ == '__main__':
    main()
