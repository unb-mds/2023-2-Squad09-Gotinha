from urllib.request import Request, urlopen
from PyPDF2 import PdfFileReader
import io
import re
import requests
import json

# Passo 1: Faz a requisição para o arquivo JSON
url1 = 'https://raw.githubusercontent.com/unb-mds/2023-2-Squad09/main/Protótipos/Extrator/22-21-20_teste.json'
response1 = requests.get(url1)

# Verifica se a requisição foi bem sucedida (código 200 indica sucesso)
if response1.status_code == 200:
    # Obtém o conteúdo JSON
    json_data1 = response1.json()

    # Não é necessário usar json.loads aqui, pois response1.json() já converte o JSON em um objeto Python
    urls_json = json_data1

    # loop para abrir cada url e extrair os dados e alocar em um arquivo
    for item in urls_json:
        # abre uma url por vez
        url = item['url']

        # Chamando funções para extrair o pdf
        remote_file = urlopen(Request(url)).read()
        memory_file = io.BytesIO(remote_file)
        pdf = PdfFileReader(memory_file, strict=False)

        # Gerando um json sem baixar o pdf no seu computador e reutilizando um arquivo para não acumular espaço
        with open('amem2.json', 'w', encoding="utf-8") as f:
            for page_num in range(pdf.numPages):
                pageObj = pdf.getPage(page_num)

                try:
                    txt = pageObj.extractText()
                    
                except:
                    pass
                else:
                    f.write(txt)
            f.close()

        # Leitura do arquivo
        with open('amem2.json', 'r', encoding='utf-8') as arquivo:
            texto_completo = arquivo.read()

        # Palavra a ser pesquisada
        palavra_alvo = 'decreto orçamentário'

        # Regex para localizar todos as aparições da palavra
        ocorrencias = re.finditer(rf'\b{re.escape(palavra_alvo)}\b', texto_completo, flags=re.IGNORECASE)

       # Extrair trechos de texto que contêm a palavra
        trechos = []
        for ocorrencia in ocorrencias:
            inicio = max(0, ocorrencia.start() - 8)  # 8 caracteres antes do início da palavra
            fim = min(len(texto_completo), ocorrencia.end() + 8000)  # 8000 caracteres após o fim da palavra
            trecho = texto_completo[inicio:fim]
            trechos.append(trecho)  

        # Imprime trechos em um arquivo 
        for trecho in trechos:
            with open('22-21-20.json', 'a', encoding="utf-8") as f:
                try:
                    txt = trecho
                    
                except:
                    pass
                else:
                    f.write(txt)
                f.close()
                
