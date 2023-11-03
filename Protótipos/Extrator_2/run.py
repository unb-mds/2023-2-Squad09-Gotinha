import subprocess
import json
import os
from pdf_json import url_Json


# Executa o spider e obtém a lista de dados
comando = "scrapy runspider /Users/yanlucas/2023-2-Squad09-Gotinha/Protótipos/Extrator_2/goiania_spider.py -o versao_reduzida.json"
resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE)

# Obtém o caminho do diretório atual
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define o caminho completo para o arquivo JSON
output_file_path = os.path.join(script_dir, "versao_reduzida.json")

# Renomeia o arquivo JSON gerado pelo scrapy para o caminho desejado
os.rename("versao_reduzida.json", output_file_path)

# Verifica se a lista de dados foi carregada corretamente
print("Execução bem-sucedida! O arquivo versao_reduzida.json foi gerado no mesmo diretório do script.")

# Caminho completo para o arquivo JSON gerado pelo scrapy
json_file_path = os.path.join(script_dir, "versao_reduzida.json")

# Chama a função url_Json com os dados lidos do arquivo JSON
url_Json(json_file_path)

print("Função url_Json foi executada")

