import re

# Função para extrair trechos de cada arquivo JSON
def extrair_trechos(arquivo_path):
    
    # Lista para armazenar os trechos filtrados
    trechos_filtrados = []

    # Expressão regular para encontrar o padrão "DECRETO ORÇAMENTÁRIO Nº" até "no valor R$"
    padrao = re.compile(r'(DE\s*CRETO\s+ORÇAMENTÁRIO\s+Nº\s*(\d+)\s*.*?R\$\s[^\n]*)', re.DOTALL)
    
    with open(arquivo_path, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
        
        # Procura por ocorrências usando regex
        ocorrencias = padrao.finditer(texto)
        
        # Adiciona os trechos após cada ocorrência
        for ocorrencia in ocorrencias:
            trecho = ocorrencia.group(1).strip()
            
            if trecho and 'saúde' in trecho.lower():
            
                n_decreto_match = re.search(r'(\d+)', trecho)
                n_decreto = n_decreto_match.group(1).lstrip('0') if n_decreto_match else None
                
                date_match = re.search(r'(\d+ [^\d]+ \d+)', trecho)
                date = date_match.group(1).replace('\n', '').strip() if date_match else None
                
                if date:
                    padrao_data = re.compile(r'(\d+)\s+DE\s+(\w+)\s*(?:DE)?\s+(\d+)')
                    correspondencia = padrao_data.search(date)

                    if correspondencia:
                        meses = {
                            'JANEIRO': 1,
                            'FEVEREIRO': 2,
                            'MARÇO': 3,
                            'ABRIL': 4,
                            'MAIO': 5,
                            'JUNHO': 6,
                            'JULHO': 7,
                            'AGOSTO': 8,
                            'SETEMBRO': 9,
                            'OUTUBRO': 10,
                            'NOVEMBRO': 11,
                            'DEZEMBRO': 12
                        }
                
                        mes = correspondencia.group(2)
                        num_mes = meses.get(mes.upper())
                        ano = correspondencia.group(3)
                
                        valor_match = re.search(r'R\$\s*([\d,.]+).', trecho)
                        valor_str = valor_match.group(1).replace('.', '').replace(',', '.')
                        valor = float(valor_str) if valor_match else 0.0
                        
                        trechos_filtrados.append({
                            #'Decreto Nº': n_decreto,
                            #'Data': date,
                            #'Trecho': trecho,
                            'Mês': num_mes,
                            'Ano': ano,
                            'Valor em R$': valor
                        })
        
    return trechos_filtrados
