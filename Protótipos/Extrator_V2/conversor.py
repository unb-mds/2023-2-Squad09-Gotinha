import json

# Função para converter dados para o formato desejado
def converter_para_formato_desejado(dados):
    resultado = {}
    for item in dados:
        ano = item["Ano"]
        mes = item["Mês"]
        valor_gasto = item["Valor em R$"]

        if ano not in resultado:
            resultado[ano] = {}

        if mes not in resultado[ano]:
            resultado[ano][mes] = {"valores_gastos": 0.0}

        resultado[ano][mes]["valores_gastos"] += valor_gasto

    return resultado

# Ler os dados de 2019 de um arquivo JSON
with open("trechos_filtrados_2019.json", "r") as arquivo_2019:
    dados_2019 = json.load(arquivo_2019)

# Ler os dados de 2020 de um arquivo JSON
with open("trechos_filtrados_2020.json", "r") as arquivo_2020:
    dados_2020 = json.load(arquivo_2020)

# Ler os dados de 2021 de um arquivo JSON
with open("trechos_filtrados_2021.json", "r") as arquivo_2021:
    dados_2021 = json.load(arquivo_2021)

# Ler os dados de 2022 de um arquivo JSON
with open("trechos_filtrados_2022.json", "r") as arquivo_2022:
    dados_2022 = json.load(arquivo_2022)

# Ler os dados de 2023 de um arquivo JSON
with open("trechos_filtrados_2023.json", "r") as arquivo_2023:
    dados_2023 = json.load(arquivo_2023)

# Converter os dados para o formato desejado
dados_formato_desejado_2019 = converter_para_formato_desejado(dados_2019)
dados_formato_desejado_2020 = converter_para_formato_desejado(dados_2020)
dados_formato_desejado_2021 = converter_para_formato_desejado(dados_2021)
dados_formato_desejado_2022 = converter_para_formato_desejado(dados_2022)
dados_formato_desejado_2023 = converter_para_formato_desejado(dados_2023)

# Juntar os dados em um único formato
dados_combinados = {"id": "goiania", "nome": "GOIANIA", "detalhe": {}}
dados_combinados["detalhe"]["2019"] = dados_formato_desejado_2019
dados_combinados["detalhe"]["2020"] = dados_formato_desejado_2020
dados_combinados["detalhe"]["2021"] = dados_formato_desejado_2021
dados_combinados["detalhe"]["2022"] = dados_formato_desejado_2022
dados_combinados["detalhe"]["2023"] = dados_formato_desejado_2023

# Salvar os dados em um arquivo JSON
with open("goiania.json", "w") as arquivo_saida:
    json.dump(dados_combinados, arquivo_saida, indent=2)