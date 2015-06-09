# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 15:30:41 2015

@author: Home

"""
import xml.etree.ElementTree as ET
import pprint

def count_tags(filename):
    tags = {}
    
    for event, elem in ET.iterparse(filename):
        if elem.tag in tags:
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
    return tags

def test():

    tags = count_tags('milwaukee_wisconsin.osm')
    pprint.pprint(tags)

if __name__ == "__main__":
    test()