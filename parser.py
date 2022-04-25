#!/usr/bin/python3
""" main parser for our converter"""

from parse_lists import parse_ul, parse_ol
from parse_heading import parse_heading


def parser(markdown):
    """ main parser for our converter"""
    html = []
    ul = []
    ol = []
    ul_flag = False
    ol_flag = False
    for line in markdown:
            if line[0] == '#':
                html.append(parse_heading(line))

            if line[0] == '*':
                ol_flag = True
                ol.append(line[2:len(line) - 1])
            else:
                ol_flag = False

            if line[0] == '-':
                ul.append(line[2:len(line) - 1])
                ul_flag = True
            else:
                ul_flag = False

            if not ul_flag and ul:
                [html.append(tag) for tag in parse_ul(ul)]
                ul = []

            if not ol_flag and ol:
                [html.append(tag) for tag in parse_ol(ol)]
                ol = []
    if ul:
        [html.append(tag) for tag in parse_ul(ul)]
    if ol:
        [html.append(tag) for tag in parse_ol(ol)]

    return html
