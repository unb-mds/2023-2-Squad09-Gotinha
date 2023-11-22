import re

# Pasta contendo os arquivos JSON
pasta_diarios = 'Diários em json'

# Função para extrair trechos de cada arquivo JSON
def extrair_trechos(arquivo_path):
    
    # Lista para armazenar os trechos filtrados
    trechos_filtrados = []

    # Expressão regular para encontrar o padrão "DECRETO ORÇAMENTÁRIO Nº" até "no valor R$"
    padrao = re.compile(r'(DECRETO ORÇAMENTÁRIO Nº\s*\d+,\s*DE.*?R\$\s[^\n]*)', re.DOTALL)

    with open(arquivo_path, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
        
        # Procura por ocorrências usando regex
        ocorrencias = padrao.finditer(texto)
        
        # Adiciona os trechos após cada ocorrência
        for ocorrencia in ocorrencias:
            trecho = ocorrencia.group(1).strip()
            
            n_decreto_match = re.search(r'(\d+)', trecho)
            n_decreto = n_decreto_match.group(1).strip() if n_decreto_match else None
            
            date_match = re.search(r'DE (\d+ [^\d]+ \d+)', trecho)
            date = date_match.group(1).strip() if date_match else None
            
            orgao_match = re.search(r'em\s*favor\s*(?:de|do|da)?[\n\s]*(.*?),', trecho, re.DOTALL | re.IGNORECASE)
            orgao = orgao_match.group(1).strip() if orgao_match else None
            
            valor_match = re.search(r'R\$\s*([\d,.]+).', trecho)
            valor = valor_match.group(1).strip() if valor_match else None
            
            trechos_filtrados.append({
                'Decreto Nº': n_decreto,
                'Data': date,
                'Órgão': orgao,
                'Valor em R$': valor
                
            })
        
    return trechos_filtrados
