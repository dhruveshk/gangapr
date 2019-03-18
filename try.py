#!/usr/bin/env python
import os
import sys
import PyPDF2 as pd



pstr = os.popen('pdf2txt.py /home/gangapr/'+str(sys.argv[1])).read()
c = len(re.findall("(?<![a-z])the(?![a-z])",pstr,re.IGNORECASE))
with open("tryout.txt", 'w') as f:
    f.writelines(str(c))
