#!/usr/bin/python3
""" contains modules that parse and convert markdown to html """


def handle_heading(text, level):
    """ return heading with certain level containing passed in text """
    return "<h{}>{}</h{}>".format(level, text, level)


def parse_heading(line):
    """
    parses heading in markdown and calls handle_heading to convert it to html \
    """
    if line[:1] == "#" and line[1] == ' ':
        return handle_heading(line[2:len(line) - 1], 1)
    if line[:2] == "##" and line[2] == ' ':
        return handle_heading(line[3:len(line) - 1], 2)
    if line[:3] == "###" and line[3] == ' ':
        return handle_heading(line[4:len(line) - 1], 3)
    if line[:4] == "####" and line[4] == ' ':
        return handle_heading(line[5:len(line) - 1], 4)
    if line[:5] == "#####" and line[5] == ' ':
        return handle_heading(line[6:len(line) - 1], 5)
    if line[:6] == "######" and line[6] == ' ':
        return handle_heading(line[7:len(line) - 1], 6)
