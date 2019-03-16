#!/usr/bin/env python
import PyPDF2 as pd
pdfst = open('CERN.pdf', 'rb')
pdfo = pd.PdfFileReader(pdfst)
for i in range(0,pdfo.numPages):
    pgo = pdfo.getPage(i)
    f = open("cern"+str(i)+".pdf","wb")
    pdfw = pd.PdfFileWriter()
    pdfw.addPage(pgo)
    pdfw.write(f)
    f.close()
pdfst.close()
pm = CustomMerger()
pm.files = ['tryout.txt']
pm.overwrite = True
pm.module = 'pdfmerger.py'
argl = []
for i in range(0,12):
    argl.append(['cern{}.pdf'.format(i),i])
s = ArgSplitter(args=argl)
j = Job(splitter=s)
j.outputfiles = ['tryout.txt']
j.application.exe = File('try.py')
j.merger = pm
j.postprocessors.append(pm)
j.submit()
