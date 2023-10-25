# Release 1

## Introdução

Este projeto faz parte da disciplina de Métodos de Desenvolvimento de Software (MDS) e tem como principal objetivo tornar os Diários Oficiais dos municípios do Estado de Goiás mais 
acessíveis por meio de uma plataforma web. O projeto oferece diversas funcionalidades para facilitar a busca de informações e também para analisar os dados de forma estatística.

A importância desse projeto está na ideia de tornar a informação do governo mais transparente e acessível a todos. 

### Nosso Objetivo

Nosso projeto "Gotinha" tem como principal objetivo a coleta de informações relacionadas aos gastos com saúde nos municípios de Goiás a partir dos Diários Oficiais. 

Utilizando um backend equipado com um Web Scraper, a biblioteca PyPDF2 e expressões regulares (regex), nós processaremos e estruturaremos esses dados. Em seguida, apresentaremos 
essas informações de forma acessível aos usuários por meio de uma interface desenvolvida em React.

Essa interface permitirá que os usuários realizem pesquisas sobre seus respectivos municípios, façam comparações entre diferentes localidades e tenham uma visão clara sobre quais
cidades estão investindo mais em saúde. Tudo de maneira intuitiva e simples de entender.

### Tecnologias escolhidas e justificativa

O "Querido Diário" utiliza o Regex e o Scrapy para a extração de informações dos Diários Oficiais. O Regex é útil para identificar padrões nos textos, enquanto o Scrapy automatiza a coleta de dados de páginas da web.

O uso do PyPDF2 se mostrou a escolha mais funcional para a análise de documentos em PDF, como os Diários Oficiais.

Para o desenvolvimento da interface de usuário, optamos pelo React. Essa escolha se baseou no fato de que nenhum dos membros da equipe tinha experiência em frontend, e o React foi recomendado pelo monitor devido à sua documentação extensa e ampla aceitação na comunidade de desenvolvimento.

### Produtos Entregues

1. **Conversor de PDF para JSON [Link](https://github.com/unb-mds/2023-2-Squad09/tree/main/Prot%C3%B3tipos/Conversor_PDF_TXT)**
2. **Protótipo de Baixa Fidelidade [Link](https://github.com/unb-mds/2023-2-Squad09/tree/main/Prot%C3%B3tipos/Prot%C3%B3tipo_Baixa_Fidelidade)**
3. **Protótipo de Alta Fidelidade [Link](https://github.com/unb-mds/2023-2-Squad09/tree/main/Prot%C3%B3tipos/Prot%C3%B3tipo_Alta_Fidelidade)**
4. **Protótipo de Filtro [Link](https://github.com/unb-mds/2023-2-Squad09/tree/main/Prot%C3%B3tipos/Prot%C3%B3tipo_Filtro)**
5. **Protótipo Selenium [Link](https://github.com/unb-mds/2023-2-Squad09/tree/main/Prot%C3%B3tipos/Prot%C3%B3tipoSelenium)**
6. **Extrator [Link](https://github.com/unb-mds/2023-2-Squad09/tree/main/Prot%C3%B3tipos/Extrator)**

### Tópicos Estudados

Durante o desenvolvimento inicial do projeto, realizamos estudos abrangendo os seguintes tópicos:

- API
- GitHub
- Docker
- Arquitetura de Software
- Requisitos de Software
- Visão de Software
- GitPages
- Kanban
- Pandas
- Regex
- Scrapy
- Snippet
- Parser
- Requisitos
- Scrum

## Desafios

**Dificuldade com a configuração do ambiente de desenvolvovimento**

**Versionamento pypdf2 (Versão especifica)**

**Dificuldades com o linux**

**Dificuldades com o React**


## Solução Proposta

As dificuldades relacionadas ao PyPDF2 e à configuração do ambiente foram solucionadas.

A proposta para os membros sem experiência no Linux foi a utilização do WSL (Windows Subsystem for Linux).

Estudos sobre o React estão sendo realizados por todos os membros da equipe para a conclusão do projeto.

## Histórico de Versão

| Versão | Alteração              | Responsável      | Revisor            | Data       |
|--------|------------------------|------------------|--------------------|------------|
| 1.0    | Release 1              | Marcio Guilherme | João Artur Leles   | 24/10/2023 |
