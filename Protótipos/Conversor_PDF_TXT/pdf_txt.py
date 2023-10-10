from PyPDF2 import PdfFileReader, PdfFileWriter

file_path = 'diario_oficial_2023-10-05_completo.pdf'
pdf = PdfFileReader(file_path)

with open('diario_copia.txt','w',encoding="utf-8") as f:
    for page_num in range(pdf.numPages):
        print('page: {0}'.format(page_num+1))
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
            print(''.center(100,'-'))
        except:
            pass
        else:
            f.write('page{0}\n0'.format(page_num+1))
            f.write(''.center(100,'-'))
            f.write(txt)
    f.close()
