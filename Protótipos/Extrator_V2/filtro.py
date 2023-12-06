import re

# Pasta contendo os arquivos JSON
pasta_diarios = 'Diários em json'

# Função para extrair trechos de cada arquivo JSON
def extrair_trechos(arquivo_path):
    
    # Lista para armazenar os trechos filtrados
    trechos_filtrados = []

    # Expressão regular para encontrar o padrão "decreto orçamentário" até "no valor R$"
    padrao = re.compile(r'(DECRETO ORÇAMENTÁRIO.*?R\$\s[^\n]*)', re.DOTALL)
    
    with open(arquivo_path, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
        # Procura por ocorrências usando regex
        ocorrencias = padrao.finditer(texto)
        # Adiciona os trechos após cada ocorrência
        for ocorrencia in ocorrencias:
            trecho = ocorrencia.group(1).strip()
            if trecho:
                trechos_filtrados.append({'Trecho': trecho})
        
    return trechos_filtrados
