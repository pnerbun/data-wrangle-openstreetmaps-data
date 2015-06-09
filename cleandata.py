# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 17:20:25 2015

@author: Home
"""

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "milwaukee_wisconsin.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "Way"]

mapping = { "St": "Street",
            "St.": "Street",
            "Rd": "Road",
            "Rd.": "Road",
            "Ave": "Avenue",
            "Ave.": "Avenue",
            "Blvd" : "Boulevard",
            "Ct" : "Court",
            "Dr" : "Drive",
            "Dr." : "Drive",
            "Pkwy" : "Parkway",
            "Pl." : "Place"
            }

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    return street_types


def update_name(name, mapping):
    """this function will update the street name and make street names consistent"""
    name = name.replace(",", "")
    for word in name.split(" "):
        if word in mapping.keys():
            name = name.replace(word, mapping[word])

    return name

def test():
    st_types = audit(OSMFILE)
    #pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name
            if name == "Milwaukee Ave":
                assert better_name == "Milwaukee Avenue"
            if name == "Miller Pkwy":
                assert better_name == "Miller Parkway"
    print "Pass"

if __name__ == '__main__':
    test()