import json
from docx import Document
import os
from urllib.request import urlopen, Request
import io

def docx_to_json(item, output_directory):
    try:
        ed = item['Decreto']
        data = item['Data']
        url = item['URL']

        print(f"Processando Decreto {ed} - Data {data} - URL {url}")

        # Baixa o arquivo DOCX
        remote_file = urlopen(Request(url)).read()
        memory_file = io.BytesIO(remote_file)

        # Carrega o arquivo DOCX
        doc = Document(memory_file)

        # Extrai o texto do arquivo DOCX e substitui caracteres não imprimíveis
        text = ""
        for paragraph in doc.paragraphs:
            paragraph_text = paragraph.text.replace('\r', '').replace('\n', '')
            text += ''.join(char if char.isprintable() or char.isspace() else '' for char in paragraph_text) + "\n"

        # Cria o nome do arquivo
        file_name = f"{ed}_{data}.json"
        file_path = os.path.join(output_directory, file_name)

        # Salva o texto em um arquivo JSON
        with open(file_path, 'w', encoding="utf-8") as json_file:
            json_file.write(text)

        print("Conversão concluída.")

    except Exception as e:
        print(f"Erro durante o processamento: {e}")

# Exemplo de utilização
output_directory = "Decretos em json/Decretos_2023"
items = [
    {"Decreto": "191", "Data": "13 DE JUNHO DE 2023", "URL": "https://www.luziania.go.gov.br/wp-content/uploads/2023/06/DECRETO-ORCAMENTARIO_191_2023-JUNHO.docx"},
    {"Decreto": "190", "Data": "13 DE JUNHO DE 2023", "URL": "https://www.luziania.go.gov.br/wp-content/uploads/2023/06/DECRETO-ORCAMENTARIO_190_2023-JUNHO.docx"},
    {"Decreto": "189", "Data": "13 DE JUNHO DE 2023", "URL": "https://www.luziania.go.gov.br/wp-content/uploads/2023/06/DECRETO-ORCAMENTARIO_189_2023-JUNHO.docx"},
    {"Decreto": "188", "Data": "12 DE JUNHO DE 2023", "URL": "https://www.luziania.go.gov.br/wp-content/uploads/2023/06/DECRETO-ORCAMENTARIO_188_2023-JUNHO.docx"},
    {"Decreto": "187", "Data": "12 DE JUNHO DE 2023", "URL": "https://www.luziania.go.gov.br/wp-content/uploads/2023/06/DECRETO-ORCAMENTARIO_187_2023-JUNHO-1.docx"}
]

for item in items:
    docx_to_json(item, output_directory)
