#!/usr/bin/env python
import os
import sys
import PyPDF2 as pd



pstr = os.popen('pdf2txt.py /home/gangapr/'+str(sys.argv[1])).read()
c = pstr.count("the")
with open("tryout.txt", 'w') as f:
    f.writelines(str(c))
