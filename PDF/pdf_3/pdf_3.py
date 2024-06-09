from PyPDF2 import PdfFileReader, PdfFileMerger

meger = PdfFileMerger() # 여러 PDF 파일을 하나로 병합할 때 사용하는 클래스
meger.append(PdfFileReader(open('file1.pdf', 'rb')))
meger.append(PdfFileReader(open('file2.pdf', 'rb')))
meger.write('file1_2_merge.pdf')