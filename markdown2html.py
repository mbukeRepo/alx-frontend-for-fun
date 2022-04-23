#!/usr/bin/python3
"""
Python implementation of a converter that converts
markdown to html
"""

import sys
from parse_heading import parse_heading
from write_to_file import write_to_file


def main():
    """ main enty point to my program """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    try:
        markdown = open(sys.argv[1])
        html = []
        for line in markdown:
            html.append(parse_heading(line))

        dest_file = open(sys.argv[2], 'w')
        write_to_file(dest_file, html)

        dest_file.close()
        markdown.close()
        print("opened and closed markdown successfully")
    except FileNotFoundError:
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)

if __name__ == "__main__":
    main()
