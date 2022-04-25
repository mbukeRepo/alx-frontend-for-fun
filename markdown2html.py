#!/usr/bin/python3
"""
Python implementation of a converter that converts
markdown to html
"""

import sys
from parse_heading import parse_heading
from write_to_file import write_to_file
from parse_lists import parse_ul


def main():
    """ main enty point to my program """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
    try:
        markdown = open(sys.argv[1])
        html = []
        ul = []
        ul_flag = False
        for line in markdown:
            if line[0] == '#':
                html.append(parse_heading(line))
            if line[0] == '-':
                ul.append(line[2:len(line) - 1])
                ul_flag = True
            else:
                ul_flag = False
            if not ul_flag and ul:
                [html.append(tag) for tag in parse_ul(ul)]
                ul = []
        if ul:
            [html.append(tag) for tag in parse_ul(ul)]
        dest_file = open(sys.argv[2], 'w')
        write_to_file(dest_file, html)

        dest_file.close()
        markdown.close()
    except FileNotFoundError:
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit(1)

if __name__ == "__main__":
    main()
