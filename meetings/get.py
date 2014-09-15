#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import urllib2, html5lib
from lxml import etree

def localtree(url):
    with open(url, 'r') as f:
        parser = html5lib.HTMLParser(\
                tree=html5lib.treebuilders.getTreeBuilder("lxml"),\
                namespaceHTMLElements=False)
        root = parser.parse(f)
    return root

def headtree(root):
    print etree.tostring(root)[0:200]

def webpage(f):
    parser = html5lib.HTMLParser(\
        tree=html5lib.treebuilders.getTreeBuilder("lxml"),\
        namespaceHTMLElements=False)
    root = parser.parse(f)
    return root

def text(root, x):
    elem = root.xpath(x)[0]
    e = list(elem.itertext())
    return e
