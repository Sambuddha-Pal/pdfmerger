import PyPDF2
pdfiles = ["15.pdf","16.pdf","20.pdf"]
pdfMerge = PyPDF2. PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2. PdfReader(pdfFile)
    pdfMerge. append(pdfReader)
pdfFile. close()
pdfMerge. write('merged.pdf')