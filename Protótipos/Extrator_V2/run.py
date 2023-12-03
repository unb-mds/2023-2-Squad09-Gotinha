import subprocess
import json
import os
from pdf_json import url_Json
from filtro import extrair_trechos
from goiania_spider import GoianiaSpider

# Executa o spider e obtém os diários em .json
# Lembre-se de navegar pelo terminal até o diretório onde está localizado o arquivo goiania_spider.py

# Criando uma instância do spider
spider_instance = GoianiaSpider()

# Acessando a variável 'year' do spider
year = spider_instance.start_requests().__next__().url.split('=')[-1]

# Obtém o caminho do diretório atual
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define o caminho completo para o arquivo JSON
output_file_path = os.path.join(script_dir, f"Edições por Ano/edicoes_{year}.json")

# Renomeia o arquivo JSON gerado pelo scrapy para o caminho desejado
os.rename(f"Edições por Ano/edicoes_{year}.json", output_file_path)

# Verifica se a lista de dados foi carregada corretamente
print(f"Execução bem-sucedida! O arquivo 'edicoes_{year}.json' foi gerado.")

# Caminho completo para o arquivo JSON gerado pelo scrapy
json_file_path = os.path.join(script_dir, f"Edições por Ano/edicoes_{year}.json")

# Chama a função url_Json com os dados lidos do arquivo JSON
url_Json(json_file_path)
print("Execução da função url_Json foi bem-sucedida!")

# Pasta contendo os arquivos JSON
pasta_diarios = os.path.join(script_dir, f"Diários em json/diarios_{year}")

# Lista para armazenar os trechos filtrados
trechos_filtrados = []

# Itera sobre cada arquivo na pasta
for arquivo_nome in os.listdir(pasta_diarios):
    if arquivo_nome.endswith('.json'):
        arquivo_path = os.path.join(pasta_diarios, arquivo_nome)
        trecho = extrair_trechos(arquivo_path)
        for item in trecho:
            trechos_filtrados.append(item)
            
# Cria a string JSON sem formatação
json_str = json.dumps(trechos_filtrados, default=str, ensure_ascii=False, indent=None)

# Adiciona quebras de linha após cada `},`
json_str = json_str.replace('},', '},\n')

# Adiciona uma quebra de linha no início
json_str = json_str.replace('[', '[\n ')

# Adiciona uma quebra de linha no final
json_str = json_str.replace(']', '\n]')

# Cria o caminho completo para a pasta "filtrados"
filtered_directory = os.path.join(script_dir, "filtrados")

# Verifica se o diretório "filtrados" existe, se não, cria
if not os.path.exists(filtered_directory):
    os.makedirs(filtered_directory)

# Salva os trechos filtrados em um novo arquivo JSON na pasta "filtrados"
filtered_file_path = os.path.join(filtered_directory, f"trechos_filtrados_{year}.json")

# Salva os trechos filtrados em um novo arquivo JSON
with open(filtered_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(json_str)
print(f"Execução do filtro bem-sucedida! O arquivo 'trechos_filtrados_{year}.json' foi gerado")
