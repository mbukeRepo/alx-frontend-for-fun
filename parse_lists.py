#!/usr/bin/python3
""" contains implementation for list parsing """


def parse_ul(ul):
    """ help in parsing ul"""
    new_ul = ['<ul>']
    [new_ul.append('<li>{}</li>'.format(li)) for li in ul]
    new_ul.append('</ul>')
    print(new_ul)
    return new_ul