# Relatório de Testes - Extrator_V2

## O que foi feito?

### Testes de Regressão
Os Testes de Regressão foram aplicados para verificar se as alterações recentes no código impactaram negativamente o funcionamento dos métodos. Dessa forma, garantimos que o Extrator_V2 continue a desempenhar suas funções fundamentais mesmo após modificações.

### Testes de Cobertura de Código
A implementação dos Testes de Cobertura de Código é crucial para avaliar a extensão da verificação do código-fonte. Esse conjunto de testes verifica não apenas se o código está funcionando corretamente, mas também se está sendo abrangente o suficiente para lidar com diferentes cenários.

### Testes Unitários
Os Testes Unitários foram aplicados para garantir que cada parte individual do Extrator_V2 esteja operando corretamente. Desde a extração de dados até o processamento de informações, cada unidade foi testada para assegurar sua funcionalidade independente.

## Por que é Importante Testar?

### Garantia de Qualidade:
Os testes são essenciais para manter e elevar os padrões de qualidade do código. Eles ajudam a evitar a introdução de bugs e erros, proporcionando maior confiabilidade ao Extrator_V2.

### Manutenção Sustentável:
Testar torna a manutenção do código mais fácil. Com uma suíte de testes robusta, é possível efetuar alterações e melhorias com confiança, sabendo que os testes ajudarão a identificar quaisquer impactos negativos.

### Entendimento do Código:
Os testes servem como documentação viva do comportamento esperado do código. Facilitam o entendimento do funcionamento do Extrator_V2, tornando-o mais acessível para futuros desenvolvedores.

### Rastreabilidade e Análise:
Através dos resultados dos testes, podemos rastrear e analisar a cobertura do código. Isso não apenas valida a eficácia do código atual, mas também orienta o desenvolvimento futuro.

Em resumo, os testes desempenham um papel crucial na construção e manutenção de projeto robusto e confiável. Essa abordagem proativa não só garante a funcionalidade atual, mas também estabelece uma base sólida para futuras melhorias e expansões do projeto Gotinha.

## Como funciona o pytest?

Organize seu projeto da seguinte forma:

1. Crie uma pasta chamada `tests` na raiz do projeto para armazenar os arquivos de teste.

2. Dentro da pasta `tests`, crie arquivos com o padrão `test_*.py`, onde `*` é um nome descritivo para o teste.

## Escrevendo Testes

Em cada arquivo `test_*.py`, escreva funções de teste. Essas funções geralmente começam com `test_`. Use afirmações `assert` para verificar se os resultados esperados coincidem com os resultados reais.

Exemplo (`test_calculadora.py`):

# tests/test_calculadora.py

def test_soma():
    assert 1 + 1 == 2

def test_subtracao():
    assert 3 - 1 == 2

## Executando Testes

Abra um terminal na raiz do seu projeto.

Execute os comandos :
```
cd Protótipos
cd Extrator_V2
coverage report -m --include="tests/*"
```

O pytest encontrará automaticamente todos os arquivos de teste e executará as funções de teste.


## Assertions e Resultados
Se todas as afirmações `assert` passarem sem erros, os testes serão considerados bem-sucedidos.

Caso contrário, o pytest fornecerá informações detalhadas sobre os testes falhados, incluindo mensagens de erro e rastreamentos de pilha.

## Comandos do Coverage.py

coverage run -m pytest - Comando para executar junto ao pytsest

coverage report -m - Gera planilha com resultados dos testes dentro do cmd

coverage html - Gera relatorios na e cria arquivos na pasta "htmlcov"


## Detalhes Técnicos

A biblioteca pytest foi utilizada para testar os funcionamentos de métodos e extrações do Extrator_V2, junto à biblioteca pytest. Também foram utilizadas as seguintes bibliotecas:

- `pip install -U pytest`
- `pip install scrapy`
- `pip install PyPDF2`
- `pip install coverage`

Os testes feitos nas classes do extrator, chamados de:

- `test_filtro.py`
- `test_goiania_spider.py`
- `test_pdf_json.py`
- `test_run.py`

Foram os seguintes tipos de testes:

- **Teste de Regressão:** Garante que o método continue funcionando conforme esperado após alterações recentes no código.
- **Teste de Cobertura de Código:** Verifica se é mantida uma cobertura do código, incluindo casos em que a resposta não é válida.
- **Teste Unitário:** Garante o correto funcionamento de cada uma das unidades do código.

Após realizar os testes, obtivemos os seguintes resultados com o pytest e o covareg.py no nosso index:

Coverage report: 90%

| File                        | Stmts | Miss | Cover | Missing       |
|-----------------------------|-------|------|-------|---------------|
| tests/test_filtro.py        | 25    | 5    | 80%   | 12-18, 39, 43 |
| tests/test_goiania_spider.py | 24    | 1    | 96%   | 59            |
| tests/test_pdf_json.py       | 7     | 1    | 86%   | 9             |
| tests/test_run.py            | 28    | 1    | 96%   | 52            |
| **TOTAL**                   | **84**| **8**| **90%**| -  |


Um boa cobertura julgando o tamanho do projeto. Pytest e covarege.py são bibliotecas simples e viáveis de serem utilizadas no projeto.