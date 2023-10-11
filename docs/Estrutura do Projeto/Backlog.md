# Requisitos 

## 1. Elicitação

### 1.1 Personas
A partir de agora, iremos referir-nos aos "cidadãos", aos "estudantes", aos "pesquisadores (academia)", aos "jornalistas" e aos "gestores públicos",  como os principais "usuários" do projeto. Ao utilizar essa terminologia, buscamos destacar a centralidade desses grupos em nossa abordagem, reconhecendo que suas necessidades, desafios e expectativas serão o foco principal durante o desenvolvimento do projeto.

### 1.2 Requisitos Não Funcionais (RNF)

|   Tipo   | Código | Requisito |
|   -     |    -    |    -      |
|    Confiabilidade    |   RNF1   | O sistema deve ser transparente e garantir que a informação disponibilizada não seja alterada|
|    Escalabilidade     |   RNF2   | O sistema deve ser consistente para suportar um número considerável de usuários e atividades simultâneas a partir da implementação de uma arquitetura de software escalável. |
|    Usabilidade     |   RNF3    | O conteúdo de interface da aplicação deve ser totalmente responsivo para web. |
|    Usabilidade     |   RNF4    | O sistema deve ser acessível, conforme as diretrizes de acessibilidade para conteúdo web (WCAG) do W3C. |
|    Performance     |   RNF5   | O sistema deve ser rápido e eficiente, proporcionando uma experiência satisfatória ao usuário a partir de constantes otimizações no código. |
| Requisitos de Interface |   RNF6    |    cores?  verde, branco, preto   |
<p align="center">Tabela 1. Requisitos Não Funcionais</p>

### 1.3 Requisitos Funcionais (RF)

| Épico  | Feature | História de usuário | Critério de aceitação|
|   -     |    -   |         -           |           -          |
| EP01 - Tratamento dos dados do Diário Oficial | F01 - Extrair Diário Oficial | US01- Eu como usuário, gostaria de ter acesso a um diario oficial, para assim poder verificar irregularridades | Qualquer usuário deverá visualizar o diário oficial solicitado <br/><br/> O diário oficial deve estar restrito aos municípios do Estado do Goiás <br/><br/> O diário oficial deve ser referente a qualquer data válida |
| EP01 - Tratamento dos dados do Diário Oficial | F02 - Gerenciamento de dados    |    US02 - Eu como usuário, gostaria de filtrar as informações, para melhor visualização dos dados, de forma rápida e fácil  | Deve haver um campo de pesquisa para filtragem de informações;<br/><br/>Ao inserir as palavras chaves e solicitar a busca deve se retornar informações sobre a mesma<br/><br/> As informações devem ser retornadas para visualização em forma de lista|
<p align="center">Tabela 2. Requisitos Funcionais</p>

## Histórico de Versão

| Versão | Alteração |  Responsável  | Revisor | Data  |
| ------ | :-------: | :-----------: | :-----: | :---: |
|  1.0   | Listando Requisitos | João, Maria, Paulo |  -   | 22/09/23 |
|  1.1   | Modificação nos Requisitos Funcionais e Não Funcionais | João | - | 08/10/23