from urllib.request import Request, urlopen
from PyPDF2 import PdfFileReader
import io
import requests
import json
import os

# Obtém o diretório atual do script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define o nome do subdiretório para armazenar os arquivos
output_subdirectory = 'Diários em json'

# Combina o diretório atual com o subdiretório de saída
output_directory = os.path.join(script_dir, output_subdirectory)

# Verifica se o diretório de saída existe, se não, cria
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def url_Json(arquivo):
    # Lê o arquivo JSON local
    with open(arquivo, 'r', encoding="utf-8") as f:
        json_data = json.load(f)

        urls_json = json_data

        for item in urls_json:
            # abre uma url por vez
            url = item['URL']
            ed = item['Edicao']
            data = item['Data']

            # Chamando funções para extrair o pdf
            remote_file = urlopen(Request(url)).read()
            memory_file = io.BytesIO(remote_file)
            pdf = PdfFileReader(memory_file, strict=False)

            # Editar o nome do arquivo e salvar dentro do diretorio "Diários em json"
            file_name = f"{ed}_{data}.json"                    
            file_path = os.path.join(output_directory, file_name)

            # Gerando um json para cada pdf aberto pela url
            with open(file_path, 'w', encoding="utf-8") as f:
                for page_num in range(pdf.numPages):
                    pageObj = pdf.getPage(page_num)

                    try:
                        txt = pageObj.extractText()

                        # Substitui caracteres não imprimíveis por espaços em branco
                        txt = ''.join(char if char.isprintable() or char == '\n' else ' ' for char in txt)
                        
                    except:
                        pass
                    else:
                        f.write(txt)
                
