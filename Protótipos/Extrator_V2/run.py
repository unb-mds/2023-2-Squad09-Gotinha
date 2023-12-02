import subprocess
import json
import os
from pdf_json import url_Json
from filtro import extrair_trechos

# Executa o spider e obtém os diários em .json
# Lembre-se de navegar pelo terminal até o diretório onde está localizado o arquivo goiania_spider.py
comando = "scrapy runspider /2023-2-Squad09-Gotinha/Protótipos/Extrator_V2/goiania_spider.py -o edicoes_2023.json"
resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE)

# Obtém o caminho do diretório atual
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define o caminho completo para o arquivo JSON
output_file_path = os.path.join(script_dir, "Edições por Ano/edicoes_2023.json")

# Renomeia o arquivo JSON gerado pelo scrapy para o caminho desejado
os.rename("Edições por Ano/edicoes_2023.json", output_file_path)

# Verifica se a lista de dados foi carregada corretamente
print("Execução bem-sucedida! O arquivo 'edicoes_2023.json' foi gerado.")

# Caminho completo para o arquivo JSON gerado pelo scrapy
json_file_path = os.path.join(script_dir, "Edições por Ano/edicoes_2023.json")

# Chama a função url_Json com os dados lidos do arquivo JSON
url_Json(json_file_path)
print("Execução da função url_Json foi bem-sucedida!")

# Pasta contendo os arquivos JSON
pasta_diarios = os.path.join(script_dir, 'Diários em json/diarios_2023')

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

# Salva os trechos filtrados em um novo arquivo JSON no mesmo diretório do script
filtered_file_path = os.path.join(script_dir, 'Diários em json/diarios_2023/trechos_filtrados_2023.json')

# Salva os trechos filtrados em um novo arquivo JSON
with open(filtered_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(json_str)
print("Execução do filtro bem-sucedida! O arquivo 'trechos_filtrados_2023.json' foi gerado")
