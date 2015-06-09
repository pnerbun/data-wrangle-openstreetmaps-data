# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 16:21:49 2015

@author: Home
"""

import xml.etree.ElementTree as ET
import pprint

def get_user(element):  
    return

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if "uid" in element.attrib:
            users.add(element.attrib["uid"])
    return users

def test():
    users = process_map('milwaukee_wisconsin.osm')
    pprint.pprint(users)
    print len(users)


if __name__ == "__main__":
    test()