# Transformar PDFs do Diário Oficial em TXT

- O formato TXT é bastante usado no Querido Diário por ser mais flexivel e fácil de manipular. Considerando isso é importante converter os arquivos disponibilizados em PDF para este formato.

## Uso do PyPDF2:

- Se mostrou uma ferramenta de fácil acesso e utilização durante os testes.

### instalando o PyPDF2:

- 1º Usei o python 3 através do vscode.
- 2º Dentro do terminal do vscode utilizei o comando `pip install camelot-py[base]` ou `pip3 install camelot-py[base]`.
- 2º Ainda no terminal utilizei o comando `pip install 'PyPDF2<3.0'` ou `pip3 install 'PyPDF2<3.0'` para baixar a biblioteca do PyPDF2 (Necessariamente tem que se usar o `'PyPDF2<3.0'` dessa forma, pois versões acima do 3.0 a bliblioteca é diferente).
- Caso de ainda ter duvida em relação a isso acesse [GitHub](https://github.com/camelot-dev/camelot/issues/339)


### __Código:__

```

from PyPDF2 import PdfFileReader, PdfFileWriter

file_path = 'diario_oficial_2023-10-05_completo.pdf'
pdf = PdfFileReader(file_path)

with open('diario_copia.txt','w',encoding="utf-8") as f:
    for page_num in range(pdf.numPages):
        print('page: {0}'.format(page_num+1))
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
            print(''.center(100,'-'))
        except:
            pass
        else:
            f.write('page{0}\n0'.format(page_num+1))
            f.write(''.center(100,'-'))
            f.write(txt)
    f.close()

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

- O arquivo.txt será alocado na mesma pasta que o arquivo.pdf esta.


# Problemas passados:

- tentei de diversas formas usar o Apache Tika em conjunto com o querido-diario-toolbox só que todas as tentativas deram falha,
acredito pelo fato dos dados do querido-diario-toolbox estarem desatualizados.