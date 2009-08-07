from __future__ import with_statement
from buchhalter import *

import buchhalter.parser as parser

import xml.etree.cElementTree as ET
import codecs


__all__ = ["loadAccountXmlFile",  "parseSentence"]

def loadAccountXmlFile(file):
    def traverseDOM(book,elmt,parent):
        template = TAccountTemplate( elmt.get('number'), elmt.get('sname'),
                                     elmt.get('cname'))
        book.add(template)

        for child in elmt:
            traverseDOM(book, child, elmt.get('number'))
        book.finishWay.append(elmt.get('number'))

    doc = ET.parse(file)
    book = TAccountBook()
    for c in doc.getroot():
        traverseDOM(book, c,  None)

    return book

def parseSentence(input):
    return parser.yacc.parse(input)
