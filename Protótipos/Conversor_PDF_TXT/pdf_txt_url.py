from urllib.request import Request, urlopen
from PyPDF2 import PdfFileReader, PdfFileWriter
import io

# Url aleatória somente para teste
url = 'https://goiania.go.gov.br/Download/legislacao/diariooficial/1964/do_19641231_000000080.pdf'

# Chamando funções para extrair o pdf
remote_file = urlopen(Request(url)).read()
memory_file = io.BytesIO(remote_file)
pdf = PdfFileReader(memory_file)

# Gerando um txt sem baixar o pdf no seu computador
with open('amem2.txt', 'w', encoding="utf-8") as f:
    for page_num in range(pdf.numPages):
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
            
        except:
            pass
        else:
            f.write('page{0}\n0'.format(page_num+1))
            f.write(''.center(100, '-'))
            f.write(txt)
    f.close()

# Gerando arquivo .json sem baixa o pdf no seu computador
with open('amem2.json', 'w', encoding="utf-8") as d:
    for page_num in range(pdf.numPages):
        print('page: {0}'.format(page_num+1))
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
            print(''.center(100,'-'))
        except:
            pass
        else:
            d.write('page{0}\n0'.format(page_num+1))
            d.write(''.center(100, '-'))
            d.write(txt)
    d.close()
