# Relatório de Testes de Integração - Extrator_V2
## Componentes a serem Integrados
Componente de Renderização de Dados: Verificação da exibição correta dos dados recebidos.
 * Front-end: react
 * Extrator: Python
 * Conversor: Python

## Cenários de teste:

### Teste de Integração do Extrator JSON
* Objetivo: Verificar a extração correta dos dados do formato pdf.
* Cenário de Teste 1: Extração de dados simples do Python.
* Entrada: Dados de exemplo em formato JSON.
* Saída Esperada: Objeto JavaScript com os dados extraídos corretamente.
* Resultado: Extração bem-sucedida. Dados corretamente extraídos e interpretados.

### Teste de Integração do Conversor Python
* Objetivo: Conversão dos dados extraídos pelo React usando Python.
* Cenário de Teste 1: Conversão para outro formato (exemplo: CSV).
* Entrada: Dados extraídos em objeto JSON.
* Saída Esperada: Arquivo CSV com os dados convertidos corretamente.
* Resultado: Conversão bem-sucedida. Arquivo CSV gerado contendo os dados convertidos do JSON.

## Estratégia de teste:
Abordagem  híbrida, pela disponibilidade dos componentes.

## Dados de teste:
* O Python foi testado com o pytest e o Coverage. O pytest foi usado para agilizar a integração e facilitar a execução de testes repetitivos e o coverage mostra partes do código que não foram cobertas pelos testes indicando lacunas na cobertura ou partes do código que não foram alcançadas durante os testes, além de ter um alto percentual de cobertura.

## Resultados
Os teste de integração estão com uma média de 95% de compatibilidade 
* filtro.py - 89%
* goiania_spider.py - 96%
* pdf_json.py - 86%
* run.py - 96%

# Observações
Testes do front-end: na parte da importação de bibliotecas estava dando vários erros, sobre a leitura dos métodos leitura erro foi na coversão que o framework tentava fazer de css para JavaScrivpt, na tentativa de consertar o erro na biblioreca verificamos que a pagina já estava para ser finalizada então não vailia a pena refazer, dps de uma pesquisa feita sobre os casos de testes pra react descobrir que ele não possue uma corbetura muito boa, a simulação é muito robusta, por isso não preferimos não usar.
Os testes do front-end foram feitos marjoritariamentes por testes feito a mão, simulando um usuários e resolvendo os problemas presenciados, contudo, o código está cumprindo com o seu objetivo.
