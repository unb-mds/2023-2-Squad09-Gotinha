# Documentação de Arquitetura de Software

## Descrição Geral

* No processo de desenvolvimento de software podemos encontrar diversas etapas e todas com seus propósitos muito bem definidos, uma delas que é de extrema importância é a documentação da arquitetura de software. De modo geral, ela auxilia no processo de desenvolvimento, descrevendo a estrutura geral, os componentes, as relações e as decisões-chave relacionadas à concepção e construção de um sistema de software.

## O que é arquitetura de software?

* Arquitetura é um meio de se obter uma análise antecipada para garantir que o sistema alcance os requisitos exigidos pelo cliente, tais como: desempenho, segurança, integridade, flexibilidade, etc. Portanto, uma arquitetura de software consiste na definição de suas camadas, que podem envolver entidades como: componentes de software, aplicativos externos, sistemas legados, propriedades externas, etc.

* A arquitetura de software é frequentemente representada por meio de diagramas, como diagramas de componentes, diagramas de sequências, diagramas de classes, entre outros, que ajudam a visualizar a estrutura e as interações do sistema.

* Ela atua como um "esqueleto" ou "espinha dorsal" do sistema, fornecendo uma visão de alto nível da sua estrutura.

### Principais tipos de arquitetura de software

* `Layers (Camadas):` Cada uma das camadas tem funcionalidades específicas no software, o que traz mais flexibilidade para a aplicação. Oferece maior facilidade de desenvolvimento e execução de testes, mas pode ter a escalabilidade comprometida principalmente a partir do momento em que o projeto começa a acumular uma quantidade elevada de camadas. Esse padrão é mais utilizado em programas de e-commerce;

* `Cliente-server (Cliente-servidor):` O processamento da informação se divide em módulos e processos distintos, combinando dados do cliente e do servidor. Um dos módulos é responsável pela manutenção da informação e o outro pela obtenção de dados. Este tipo de arquitetura de software é bastante usado em aplicativos com rotinas de usuários como de bancos e e-mail;

* `Model-View-Controller (MVC):` Separa o projeto do software em três camadas independentes: o modelo (manipulação da lógica de dados), a visão (a interface do usuário) e o controlador (fluxo de aplicação). Esta separação facilita a manutenção do código, que pode ser reutilizado em outros projetos, proporcionando um modelo interativo para o sistema.

* Além desses, existem várias outros tipos, como por exemplo: Microservices, Pipes-and-filters (PF), Peer-to-Peer (P2P), Service-Oriented Architecture (SOA), etc.

## Por que devo documentar a arquitetura de software? 

Algumas razões pelas quais é crucial documentar a arquitetura de software:

* **Facilita a Compreensão:** A documentação fornece uma descrição detalhada da estrutura e do funcionamento do software, permitindo que os membros da equipe entendam como o sistema é projetado e como os componentes se relacionam;

* **Comunicação Eficaz:** Permite que os desenvolvedores, gerentes de projeto, clientes e outras partes interessadas comuniquem-se de forma mais eficaz sobre os aspectos técnicos do projeto;

* **Facilita a Manutenção:** Quando a documentação está disponível, é mais fácil para a equipe de manutenção entender como o sistema funciona, o que agiliza a identificação e correção de problemas;

* **Transparência:** Uma documentação clara e acessível torna a arquitetura do software transparente, permitindo que as partes interessadas entendam como o sistema foi projetado e por quê.

* Segundo Steuart Henderson Britt, "Fazer negócios sem publicidade ou projetar uma arquitetura sem documentar, é como piscar para uma garota no escuro. Você sabe que está fazendo, mas ninguém mais sabe". Essa frase demonstra a verdadeira necessidade de uma documentação. Por mais perfeita e adequada que seja sua arquitetura, será inútil para outras pessoas que não a conhecem e que não podem entendê-la bem o suficiente para manuseá-la. Portanto, a documentação se faz essencial para todos os casos.

### Exemplo de tópicos abordados em um documento:

* **Histórico:** o primeiro tópico identifica a versão do documento arquitetural e do código desenvolvido, incluindo dados sobre quem está responsável pelo projeto e o que foi trabalhado em cada etapa;

* **Visão geral de componentes:** destacar os principais componentes, formando uma visão breve sobre o que está sendo trabalhado;

* **Requisitos do projeto:** os requisitos de arquitetura são um conjunto de restrições e metas que devem ser cumpridas pelo projeto. Isso inclui requisitos funcionais e não funcionais que afetam a estrutura do sistema, como desempenho, segurança, escalabilidade e usabilidade;

* **Estrutura:** fornece uma representação detalhada da estrutura do sistema, geralmente usando diagramas. Ela destaca como os principais componentes do sistema estão organizados e como se relacionam.;

* **Fundamentação do projeto:** cada decisão aplicada ao desenvolvimento deve conter uma fundamentação de como ela foi elaborada;

* **Cenários de uso:** para facilitar o estudo de caso, temos a descrição dos cenários de potencial aplicação do software em desenvolvimento;

* **Segurança:** identificar as possíveis vulnerabilidades e descrevendo as medidas de segurança implementadas ou planejadas para proteger o sistema;

* **Mapa de lançamento:** descrição do lançamento do produto quando concluído, indicando o que é necessário para sua implementação prática.

## Links Úteis

* [Documentação de arquitetura de software: definição, função e importância](https://blog.xpeducacao.com.br/documentacao-de-arquitetura-de-software/) </br>
* [Você conhece quais são os padrões e tipos de arquiteturas de software?](https://truechange.com.br/blog/tipos-de-arquiteturas-de-software/) </br> 
* [Vídeo: Arquitetura de Software](https://www.youtube.com/watch?v=kYx1QC1XZSo&ab_channel=C%C3%B3digoFonteTV) </br>
