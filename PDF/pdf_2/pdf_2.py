# 1, 3, 5 페이지만 추출
from PyPDF2 import PdfFileReader, PdfFileWriter

with open('pdf_test1.pdf', 'rb') as PDFfile:
    reader = PdfFileReader(PDFfile)
    writer = PdfFileWriter()
    writer.addPage(reader.getPage(0))
    writer.addPage(reader.getPage(2))
    writer.addPage(reader.getPage(4))
    writer.write(open('pdf1_3_5.pdf', 'wb'))