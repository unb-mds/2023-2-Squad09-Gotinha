import json
from collections import defaultdict

# Seu JSON original
with open('filtrados/trechos_filtrados.json', 'r', encoding='utf-8') as arquivo_json:
    dados_originais = json.load(arquivo_json)

# Organiza os dados por ano
dados_por_ano = defaultdict(list)
for dado in dados_originais:
    ano = dado["Ano"]
    dados_por_ano[ano].append(dado)

# Salva os dados em arquivos separados para cada ano
for ano, dados_ano in dados_por_ano.items():
    nome_arquivo = f'dados_{ano}.json'
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_saida:
        json.dump(dados_ano, arquivo_saida, ensure_ascii=False, indent=2)
    print(f'Dados para o ano {ano} foram salvos em {nome_arquivo}')
