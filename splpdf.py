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
