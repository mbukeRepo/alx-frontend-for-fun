#!/usr/bin/python3
""" main parser for our converter"""

from parse_lists import parse_ul, parse_ol
from parse_heading import parse_heading
from parse_p import parse_p


def main_parser(markdown):
    """ main parser for our converter"""
    html = []
    ul = []
    ol = []
    p = []
    ul_flag = False
    ol_flag = False
    p_flag = False
    for line in markdown:
            if line[0] == '#':
                html.append(parse_heading(line))
                continue

            if line[0] == '*':
                ol_flag = True
                ol.append(line[2:len(line) - 1])
                continue
            else:
                ol_flag = False

            if line[0] == '-':
                ul.append(line[2:len(line) - 1])
                ul_flag = True
                continue
            else:
                ul_flag = False

            if not ul_flag and ul:
                [html.append(tag) for tag in parse_ul(ul)]
                ul = []

            if not ol_flag and ol:
                [html.append(tag) for tag in parse_ol(ol)]
                ol = []
            if line == '\n':
                if p:
                    p.append('</p>')
                    html.append("\n".join(p))
                    p = []
                    p_flag = False
                continue
            if line != "":
                if not p_flag:
                    p.append("<p>")
                    p.append(line[:-1])
                    p_flag = True
                    continue
                else:
                    p.append('<br/>')
                p_flag = True
                p.append(line)
    if ul:
        [html.append(tag) for tag in parse_ul(ul)]
    if ol:
        [html.append(tag) for tag in parse_ol(ol)]
    if p_flag:
        p.append("</p>")
    if p:
        html.append("\n".join(p))
    return html
