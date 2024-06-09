# PDF 파일에서 텍스트 추출하기
from PyPDF2 import PdfFileReader

with open('pdf_test2.pdf', 'rb') as PDFFile:
    reader = PdfFileReader(PDFFile)
    
    for i in range(reader.numPages):
        print(f'{i+1}페이지 >> \n')
        pages = reader.getPage(i)
        extracted_test = pages.extract_text()
        print(extracted_test)


'''
numPages 속성
: PdfFileReader 객체의 속성으로 PDF 페이지의 총 수를 반환

extract_text()
: PyPDF2 라이브러리에서 PDF 파일의 텍스트 콘텐츠로 추출하는데 사용되는 메서드
'''