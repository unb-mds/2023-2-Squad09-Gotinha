from urllib.request import Request, urlopen
from PyPDF2 import PdfFileReader
import io
import requests
import json
import os

output_directory = 'c:/Users/Usuário/OneDrive/Área de Trabalho/2023-2-Squad09-Gotinha/Prótotipos/Extrator_2/Diários em TXT'

url = 'https://raw.githubusercontent.com/unb-mds/2023-2-Squad09-Gotinha/main/Protótipos/Extrator_2/versao_reduzida.json'

response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()

    for item in json_data:
        url = item['URL']

        remote_file = requests.get(url).content 
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
                            
