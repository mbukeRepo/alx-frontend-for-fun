#!/usr/bin/python3
"""
contains write_to_file module
"""


def write_to_file(file_ptr, html):
    """ writes newly formed html content to html file """
    for line in html:
        file_ptr.write("{}\n".format(line))
