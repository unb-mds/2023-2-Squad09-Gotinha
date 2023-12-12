import re
import os

# Função para extrair trechos de cada arquivo JSON
def extrair_trechos(arquivo_path):
    
    # Lista para armazenar os trechos filtrados
    trechos_filtrados = []

    # Conjunto para armazenar trechos únicos
    trechos_unicos = set()

    # Expressão regular para encontrar o padrão "EXTRATO DE CONTRATO Nº" até "R$"
    padrao = re.compile(r'EXTRATO\s+DE\s+CONTRATO\s+Nº\s*(\d+)/(\d+).*?R\$\s*([\d,.]+)|R\$\s*([\d,.]+)', re.DOTALL | re.IGNORECASE)

    # Expressão regular para identificar contratos relacionados à saúde
    padrao_saude = re.compile(r'\b(?:municipal\s+de\s+)?saúde\b', re.IGNORECASE)


    # Extrair a data do nome do arquivo
    nome_arquivo = os.path.basename(arquivo_path)
    match_data_arquivo = re.search(r'(\d{4})-(\d{2})-(\d{2})', nome_arquivo)
    ano, mes, dia = match_data_arquivo.groups() if match_data_arquivo else (None, None, None)
    
    with open(arquivo_path, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
        
        # Procura por ocorrências usando regex
        ocorrencias = padrao.finditer(texto)

        # Adiciona os trechos após cada ocorrência
        for ocorrencia in ocorrencias:
            trecho = ocorrencia.group(0).strip()
            
            # Verifica se o contrato está relacionado à saúde
            if padrao_saude.search(trecho):
                # Extrair o valor diretamente após "R$"
                valor_str = ocorrencia.group(3) or ocorrencia.group(4)
                if valor_str is not None:
                    valor_str = valor_str.replace('.', '').replace(',', '')
                    
                    # Verifica se o trecho já foi adicionado
                    if trecho not in trechos_unicos:
                        # Adiciona o trecho ao conjunto de trechos únicos
                        trechos_unicos.add(trecho)
                        
                        # Converter o valor para float e dividir por 100
                        valor = float(valor_str) / 100.0

                        trechos_filtrados.append({
                            'Ano': ano,
                            'Mês': mes,
                            'Valor em R$': valor
                        })
            
            else:
                # Se a expressão 'saúde' não foi encontrada antes do valor, procurar depois
                trecho_posterior = texto[ocorrencia.end():ocorrencia.end() + 100]  # Considerando os próximos 100 caracteres
                if padrao_saude.search(trecho_posterior):
                    # Extrair o valor diretamente após "R$"
                    valor_match_posterior = re.search(r'R\$\s*([\d,.]+)', trecho_posterior, re.IGNORECASE)
                    if valor_match_posterior and valor_match_posterior.group(1) is not None:
                        valor_str_posterior = valor_match_posterior.group(1).replace('.', '').replace(',', '')

                        # Verifica se o trecho já foi adicionado
                        if trecho not in trechos_unicos:
                            # Adiciona o trecho ao conjunto de trechos únicos
                            trechos_unicos.add(trecho)

                            # Converter o valor para float e dividir por 100
                            valor_posterior = float(valor_str_posterior) / 100.0

                            trechos_filtrados.append({
                                'Ano': ano,
                                'Mês': mes,
                                'Valor em R$': valor_posterior
                            })
        
    return trechos_filtrados
