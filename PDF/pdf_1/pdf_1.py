from PyPDF2 import PdfFileReader, PdfFileWriter

with open('pdf_test1.pdf', 'rb') as PDFfile:
    reader = PdfFileReader(PDFfile)
    writer = PdfFileWriter()
    writer.addPage(reader.getPage(4))
    writer.write(open('page5.pdf', 'wb'))

'''
rb(read binary) : 파일을 바이너리 모드로 읽기 위해 사용
텍스트 파일뿐만 아니라 이미지, 동영상, 오디오 파일 등 다양한 바이너리 파일 읽을 수 있음

바이너리란?
컴퓨터가 데이터를 처리하고 저장하는 방식 중 하나

주요 예:
이미지 파일, 오디오 파일, 비디오 파일, 실행 파일, 압축 파일, 문서 파일

텍스트 파일 vs 바이너리 파일
1. 텍스트 파일 : 사람이 읽을 수 있는 형태의 데이터로 구성
예) '.txt', '.csv', '.html' 파일 등
이 파일은 주로 ASCII 또는 유니코드와 같은 문자 인코딩을 사용하여 저장

2. 바이너리 파일 : 사람이 직접 읽기 어려운 데이터로 구성되며,
컴퓨터 프로그램을 해석하여 사용
예) 이미지, 오디오, 비디오, 실행 파일 등

따라서 바이너리 파일을 처리할 때 'rb' 모드 사용하고,
텍스트 파일 읽을 때는 'r'모드 사용하여 파일의 내용을 문자열로 읽음
'''

'''
'wb' : 파일을 바이너리 모드로 쓰기 위해 사용
1. 이지 파일을 생성 또는 덮어쓸 때
2. 오오 또는 비디오 파일을 쓸 때
3. 바너리 데이터를 다룰 때

결론 : 새운 파일을 쓰기 모드로 열기
'''
