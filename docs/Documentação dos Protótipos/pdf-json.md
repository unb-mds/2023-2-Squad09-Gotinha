# Transformar PDFs do Diário Oficial em json

- O formato json é bastante usado no Querido Diário por ser mais flexivel e fácil de manipular. Considerando isso é importante converter os arquivos disponibilizados em PDF para este formato.

## Uso do PyPDF2:

- Se mostrou uma ferramenta de fácil acesso e utilização durante os testes.

### urllib:

- O urllib é uma biblioteca padrão do python, não precisando ser instalada.
- Só precisa ser chamada.

### instalando o PyPDF2:

- 1º Usei o python 3 através do vscode.
- 2º Dentro do terminal do vscode utilizei o comando `pip install camelot-py[base]` ou `pip3 install camelot-py[base]`.
- 2º Ainda no terminal utilizei o comando `pip install 'PyPDF2<3.0'` ou `pip3 install 'PyPDF2<3.0'` para baixar a biblioteca do PyPDF2 (Necessariamente tem que se usar o `'PyPDF2<3.0'` dessa forma, pois versões acima do 3.0 a bliblioteca é diferente).
- Caso de ainda ter duvida em relação a isso acesse [GitHub](https://github.com/camelot-dev/camelot/issues/339)


### __Código:__

```python

from urllib.request import Request, urlopen
from PyPDF2 import PdfFileReader, PdfFileWriter
import io

# Url aleatória somente para teste
url = 'https://goiania.go.gov.br/Download/legislacao/diariooficial/1964/do_19641231_000000080.pdf'

# Chamando funções para extrair o pdf
remote_file = urlopen(Request(url)).read()
memory_file = io.BytesIO(remote_file)
pdf = PdfFileReader(memory_file)

# Gerando arquivo .json sem baixa o pdf no seu computador
with open('amem2.json', 'w', encoding="utf-8") as d:
    for page_num in range(pdf.numPages):
        print('page: {0}'.format(page_num+1))
        pageObj = pdf.getPage(page_num)

        try:
            json = pageObj.extractText()
            print(''.center(100,'-'))
        except:
            pass
        else:
            d.write('page{0}\n0'.format(page_num+1))
            d.write(''.center(100, '-'))
            d.write(json)
    d.close()

```

- Saída no terminal para confirmar que todas as páginas foram executadas:

```
page: 1
----------------------------------------------------------------------------------------------------
page: 2
----------------------------------------------------------------------------------------------------
page: 3
----------------------------------------------------------------------------------------------------
page: 4
----------------------------------------------------------------------------------------------------
page: 5
----------------------------------------------------------------------------------------------------
page: 6
----------------------------------------------------------------------------------------------------
page: 7
----------------------------------------------------------------------------------------------------

```

- O arquivo.json será alocado na mesmo diretório que esta sendo usado.


# Problemas passados:

- tentei de diversas formas usar o Apache Tika em conjunto com o querido-diario-toolbox só que todas as tentativas deram falha,
acredito pelo fato dos dados do querido-diario-toolbox estarem desatualizados.