#!/usr/bin/python3
""" contains implementation for list parsing """


def parse_ul(ul):
    """ help in parsing ul"""
    new_ul = ['<ul>']
    [new_ul.append('<li>{}</li>'.format(li)) for li in ul]
    new_ul.append('</ul>')
    return new_ul

def parse_ol(ol):
    """help in parsing ol"""
    new_ol = ['<ol>']
    [new_ol.append('<li>{}</li>'.format(li)) for li in ol]
    new_ol.append('</ol>')
    return new_ol
