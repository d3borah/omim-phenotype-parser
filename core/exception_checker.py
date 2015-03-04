#!/usr/bin/python
# Filename: exception_checker.py
# Deborah Siegel

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import omim
import re

def main():
    f = omim.input(sys.argv[1])
   
    probablyprotein = []
    suspectprotein = []
    
    pprot = re.compile(r"^[\\*].*\bPROTEIN(?![\w-])", re.IGNORECASE)
    sprot = re.compile(r"^[#|%|\d].*\bPROTEIN(?![\w-])", re.IGNORECASE)
    
    for record in f:
        if record.title is not None:
            title = record.title[0]
            protein = re.search(pprot, title)
            if protein:
                probablyprotein.append(title)
            suspectprot = re.search(sprot,title)
            if suspectprot:
                suspectprotein.append(title)
    
    for prot in probablyprotein:
        print prot
    print
    print "The following may not actually be proteins:"
    for prot in suspectprotein:
        print prot   
                  
if __name__ == "__main__":
    main()