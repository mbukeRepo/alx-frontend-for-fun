#!/usr/bin/python3
"""
Python implementation of a converter that converts
markdown to html
"""

import sys

from sympy import li
from write_to_file import write_to_file
from parser import parser


def main():
    """ main enty point to my program """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
    try:
        markdown = open(sys.argv[1])
        html = parser(markdown)
        dest_file = open(sys.argv[2], 'w')
        write_to_file(dest_file, html)

        dest_file.close()
        markdown.close()
    except FileNotFoundError:
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit(1)

if __name__ == "__main__":
    main()
