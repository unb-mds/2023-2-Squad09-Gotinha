from urllib.request import Request, urlopen
from PyPDF2 import PdfFileReader
import io
import json
import os

output_directory = 'c:/Users/Usuário/OneDrive/Área de Trabalho/Extrator Atualizado/Diários em TXT'

local_json_file = 'c:/Users/Usuário/OneDrive/Área de Trabalho/Extrator Atualizado/versao_reduzida.json'

with open(local_json_file, 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

urls_json = json_data

for item in urls_json:
    url = item['URL']

    remote_file = urlopen(Request(url)).read()
    memory_file = io.BytesIO(remote_file)
    pdf = PdfFileReader(memory_file, strict=False)

    for page_num in range(pdf.numPages):
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
                
        except:
            pass
                
        else:
            file_name = f"{item['Edicao']}.txt"                    
            file_path = os.path.join(output_directory, file_name)
                    
            with open(file_path, 'w', encoding="utf-8") as f:
                f.write(txt)
                        
