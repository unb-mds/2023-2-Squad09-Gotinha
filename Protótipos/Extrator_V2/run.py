import subprocess
import json
import os
from pdf_json import url_Json


# Executa o spider e obtém os diários em .json
# Lembre-se de navegar pelo terminal até o diretório onde está localizado o arquivo goiania_spider.py
comando = "scrapy runspider goiania_spider.py -o edicoes_recentes.json"
resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE)

# Obtém o caminho do diretório atual
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define o caminho completo para o arquivo JSON
output_file_path = os.path.join(script_dir, "edicoes_recentes.json")

# Renomeia o arquivo JSON gerado pelo scrapy para o caminho desejado
os.rename("edicoes_recentes.json", output_file_path)

# Verifica se a lista de dados foi carregada corretamente
print("Execução bem-sucedida! O arquivo edicoes_recentes.json foi gerado no mesmo diretório do script.")

# Caminho completo para o arquivo JSON gerado pelo scrapy
json_file_path = os.path.join(script_dir, "edicoes_recentes.json")

# Chama a função url_Json com os dados lidos do arquivo JSON
url_Json(json_file_path)

print("Função url_Json foi executada")
