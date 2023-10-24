## 1. Introdução

A criação de um protótipo é ferramenta crucial no desenvolvimento de qualquer projeto. Este protótipo permite avaliar o funcionamento do conversor, ao utiliza-lo para poder obter qualquer informação contida no diário oficial.

## 2. Protótipo de Filtro

Aqui está o código Python responsável por filtrar as informações:

~~~python
import re

# Leitura do arquivo
with open('diario_copia.txt', 'r', encoding='utf-8') as arquivo:
    texto_completo = arquivo.read()

# Palavra a ser pesquisada
palavra_alvo = 'Saúde'

# Regex para localizar todos as aparições da palavra
ocorrencias = re.finditer(rf'\b{re.escape(palavra_alvo)}\b', texto_completo, flags=re.IGNORECASE)

# Extrair trechos de texto que contêm a palavra
trechos = []
for ocorrencia in ocorrencias:
    inicio = max(0, ocorrencia.start() - 350)  # 350 caracteres antes do início da palavra
    fim = min(len(texto_completo), ocorrencia.end() + 250)  # 250 caracteres após o fim da palavra
    trecho = texto_completo[inicio:fim]
    trechos.append(trecho)

# Imprime trechos
for i, trecho in enumerate(trechos):
    print(f"Trecho {i + 1}:\n{trecho}\n{'-' * 50}")

~~~

## 3. Conclusão

Este filtro é um modelo inicial, mas ele serve como um auxílio e demonstra a eficácia do conversor.

# 4. Links Úteis

- [Documentação Regex](https://docs.python.org/pt-br/3/library/re.html)
- [Estudo Regex](https://github.com/unb-mds/2023-2-Squad09/blob/main/docs/Estudos/Regex.md)

## 5. Histórico de versão

| Versão | Alteração | Responsável | Data |
| - | - | - | - |
| 1.0 | Criando documento sobre o protótipo de filtro | João Artur Leles | 10/10 |