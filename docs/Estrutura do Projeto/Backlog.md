# Requisitos 

## 1. Elicitação

### 1.1 Requisitos Funcionais (RF)

| Código | Requisito |
|   -    |    -      |
|   RF1  | A API deve coletar os diários oficiais dos municipios do Goiás |
|   RF2  | A API deve manipular os arquivos e armazenar no banco de dados |
|   RF3  | A API deve separar os dados para cada município |
|   RF4  | A API deve filtrar os dados de acordo com os topicos abordados  |
|   RF5  | A API deve mostrar um resumo das informações do topico selecionado  |
<p align="center">Tabela 1. Requisitos Funcionais</p>

### 1.2 Requisitos Não Funcionais (RNF)

| Código  | Requisito |
|   -     |    -      |
|   RNF1  | A API deve ser desenvolvida em Python usando o FastAPI |
|   RNF2  | A API deve ser RESTful |
|   RNF3  | Os dados devem ser adquiridos através de um Bot usando Selenium  |
|   RNF4  | O Scrapy será usado para extrair as informações dos diários oficiais |
|   RNF5  | O armazenamento de dados será feito em PostgreSQL   |
|   RNF6  | O filtro será realizado com o Pandas e o Matplot |
|   RNF7  | Landing Page para mostrar as informações filtradas  |
|   RNF8  | Disponibilizar no Docker   |
<p align="center">Tabela 2. Requisitos Não Funcionais</p>

## Épicos

### Épico 1: Obter e Tratar os dados do Diário Oficial

### Épico 2: Criar um segmentador

### Épico 3: Criar a API

### Épico 4: Landing Page

### Épico 5: Disponibilizar no Docker

## Histórico de Versão

| Versão | Alteração |  Responsável  | Revisor | Data  |
| ------ | :-------: | :-----------: | :-----: | :---: |
|  1.0   | Listando Requisitos | João, Maria, Paulo |  -   | 22/09/23 |