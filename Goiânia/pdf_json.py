from urllib.request import Request, urlopen
from PyPDF2 import PdfFileReader
import io
import json
import os
from goiania_spider import GoianiaSpider

# Criando uma instância do spider
spider_instance = GoianiaSpider()

# Acessando a variável 'year' do spider
year = spider_instance.start_requests().__next__().url.split('=')[-1]

# Obtém o diretório atual do script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define o nome do subdiretório para armazenar os arquivos
output_subdirectory = f"Diários em json/diarios_{year}"

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

        # [:numero_edicoes] ---> Aqui, deve ser inserido o número de edições que serão convertidas para json
        # Ao executar pela primeira vez, o número deve ser o mesmo presente em goiania_spider.py
        # Caso os diários já estejam em json, escreva 0 para não executar a função novamente
        for item in urls_json[:0]:
            # Abre uma url por vez
            url = item['URL']
            ed = item['Edicao']
            data = item['Data']
            sup = item['Suplemento ou Ed Extra']

            # Chamando funções para extrair o pdf
            remote_file = urlopen(Request(url)).read()
            memory_file = io.BytesIO(remote_file)
            pdf = PdfFileReader(memory_file, strict=False)

            # Editar o nome do arquivo e salvar dentro do diretorio "Diários em json"
            if sup == "true":
                file_name = f"{ed}_{data} - suplemento.json"                    
                file_path = os.path.join(output_directory, file_name)
            
            else:
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
                
