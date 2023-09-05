# GitHub Pages

## 1. Introdução

O GitHub Pages é um serviço de hospedagem de sites estáticos fornecido pelo GitHub, uma plataforma de hospedagem de código-fonte e colaboração para desenvolvedores. Ele permite a criação de páginas da web simples diretamente a partir de repositórios do GitHub, sem a necessidade de configurar servidores web ou infraestrutura de hospedagem separada.

Um dos principais motivos para a utilização do GitHub Pages é relacionado a documentação. A documentação é uma parte fundamental de qualquer projeto, e o GitHub Pages torna essa documentação mais acessível e utilizável para os visitantes. Além disso, ela facilita o entendimento do projeto por todos os membros e torna mais fácil a solução de problemas e a realização de manutenções.
 
## 2. Docsify

Escolher o Docsify como a ferramenta de geração de documentação para o GitHub Pages de um projeto é uma boa ideia devido a vários fatores

- Facilidade de Uso: O Docsify é notável por sua simplicidade e facilidade de uso, pois utiliza a sintaxe Markdown.
- Documentação Dinâmica: O Docsify cria documentação dinâmica que oferece uma experiência de usuário suave. Os visitantes podem navegar pelos documentos sem recarregar a página, proporcionando uma experiência de navegação mais agradável.
- Barra Lateral de Navegação Automática: O Docsify gera automaticamente uma barra lateral de navegação com base na estrutura dos arquivos de documentação Markdown. Isso torna a navegação pelos documentos intuitiva e fácil.
- Personalização Flexível: O Docsify permite personalizar o tema e o estilo da documentação para corresponder à identidade visual do projeto.

## 3. Como Editar

No Docsify, é possivel organizar a documentação do projeto pela sidebar através da criação de uma estrutura de diretórios e arquivos Markdown no repositório. A sidebar é gerada automaticamente com base na organização desses arquivos e diretórios.

Um Exemplo de como isso pode ser feito é através da sidebar usada neste [repositório](https://unb-mds.github.io/2023-2-Squad09/):

    - [Home](./)
        -  **Planejamento**
         - **Requisitos**

    - **Releases**
        - **Sprints**
            - **Sprint 0 (01/09 - 06/09)**
                - [Ata da Reunião do dia 01/09](./AtaReuniao/ataReuniao1-09.md)
                - [Comandos Git](./Estudos/ComandosGit.md)

Agora para exemplificar a adição de novas informações a documentação será adicionado um arquivo chamado teste.md a Sprint 0.

Primeiro localizamos o arquivo(para este exemplo ele estára na pasta de Estudos do repositório), após localizarmos ele nós o adicionamos na Sprint 0 da seguinte forma:

    - [Home](./)
        -  **Planejamento**
         - **Requisitos**

    - **Releases**
        - **Sprints**
            - **Sprint 0 (01/09 - 06/09)**
                - [Ata da Reunião do dia 01/09](./AtaReuniao/ataReuniao1-09.md)
                - [Comandos Git](./Estudos/ComandosGit.md)
                - [Teste](./Estudos/teste.md)

A partir disso o arquivo teste estará disponível para ser acessado pela sidebar.

## 4. Links Úteis

- [Configurando GitHub Pages](https://www.youtube.com/watch?v=_jI3782DGDc)

- [Docsify](https://docsify.js.org/#/)

- [GitHub Pages](https://pages.github.com/)

- [GitHub Pages do projeto](https://unb-mds.github.io/2023-2-Squad09/)

## 5. Histórico de Versão

| Versão | Alteração | Responsável | Revisor | Data |
| - | - | - | - | - |
| 1.0 | Criando arquivo sobre GitHub Pages | João Artur Leles | - | 05/09 |