# Exoonero

- Site: https://exoonero.org/sobre/
- Github: https://github.com/exoonero/extrator

## objetivo do Exoonero

- O projeto tem como principal objetivo coletar, transformar em texto e separar em municípios os diários oficiais municipais da Associação dos Municípios Alagoanos (AMA). Além da separação do conteúdo por município, o texto do diário de cada ente estadual é separado em atos normativos. Também iremos utilizar algoritmos computacionais para classificar e extrair informações dos atos normativos dos diários de cada município. Mais especificamente, o nosso foco será em nomeações e exonerações.

### Requisitos não-funcionais:

- **Simplicidade**: ela se traduziu em uma análise de diversos casos, onde chegamos a conclusão que poderíamos utilizar expressões regulares (ao invés de inteligência computacional, por exemplo);
- **Facilidade de utilização do código pelo QD**: com a ajuda da busca pela simplicidade, o objetivo é depender o minímo possível de bibliotecas de terceiros e focar numa API de clara e com boa documentação;
- **Replicabilidade do código para outros estados/associações de municípios**: prevemos que a solução possa ser utilizada em outros contextos apenas modificando as expressões regulares;

## Documentos

- Para tornar mais fácil o acompanhamento, o projeto foi dividido em duas fases. A primeira fase tem como principal objetivo propor e avaliar um algoritmo que permita a separação do conteúdo do diário oficial da Associação dos Municípios Alagoanos (AMA) por município. A segunda fase diz respeito a extração e monitoramento de informações relevantes, por exemplo, nomeações e exonerações.
- Doc que detalha mais sobre como foi feito essas partes: https://github.com/exoonero/extrator/blob/main/docs/README.md

-----------------------------------------------------------------------------------------------

- Nesse Doc possui o fluxo de processamento, manuseamento e funcionamento do Contêiner Apache Tika,executando Fluxo Completo com proc.sh, coleta e extração do diário, Gerando base de dados para análise, executando o extrair_diarios.py, executando testes passo a passo:
- Em resumo nesse doc esta como funciona todo o processo desde abrir o container ate fazer a extração de dados necessários
- Doc: https://github.com/exoonero/extrator/blob/main/README.md#como-montamos-o-gabarito

