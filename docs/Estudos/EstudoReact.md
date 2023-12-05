## Estudo da estrutura do REACT

React é uma biblioteca JavaScript amplamente utilizada para criar interfaces de usuário (UI) interativas e reativas. Ele é utilizado pelo Facebook e é uma parte importante do desenvolvimento web moderno.

# Estrutura

* Componentes: No coração do React estão os componentes. Os componentes são blocos de construção reutilizáveis que você cria para representar partes específicas da interface do usuário. Eles podem ser compostos em hierarquias complexas. Por exemplo, você pode ter um componente de botão, um componente de cabeçalho, um componente de lista, etc.

* Virtual DOM (VDOM): O React usa uma abstração chamada Virtual DOM para otimizar o desempenho. O VDOM é uma representação virtual da árvore de elementos reais da sua aplicação. Sempre que ocorrem mudanças nos componentes, o React compara a versão anterior do VDOM com a versão atual para determinar quais partes da interface do usuário precisam ser atualizadas. Isso evita manipulações desnecessárias do DOM real e melhora o desempenho.

* Renderização Reativa: O React é reativo. Isso significa que, quando os dados ou o estado de um componente mudam, o React atualiza automaticamente a interface do usuário para refletir essas alterações. Isso é feito usando um mecanismo de renderização eficiente.

* Estado e Propriedades: Os componentes React podem ter estado (state) e propriedades (props). O estado é uma maneira de armazenar dados que podem mudar ao longo do tempo e afetar a renderização do componente. As propriedades são valores que são passados de um componente pai para um componente filho e são usados para personalizar o comportamento do componente filho.

* Ciclo de Vida: Os componentes React têm um ciclo de vida. Isso significa que eles passam por várias fases, como montagem, atualização e desmontagem. Você pode anexar funções a essas fases para executar código específico, como buscar dados de um servidor ou realizar ações de limpeza.

* Renderização do Lado do Cliente: O React é frequentemente usado para criar aplicativos de página única (SPA) que são executados no lado do cliente. Isso significa que a renderização da interface do usuário ocorre no navegador do usuário, em vez de no servidor. O React permite criar aplicativos web interativos e dinâmicos sem a necessidade de recarregar a página.

* Ecossistema Rico: O React possui um ecossistema rico de bibliotecas e ferramentas, incluindo o React Router para gerenciamento de rotas, Redux para gerenciamento de estado, Material-UI e Bootstrap para estilização, entre outros.

# Como utilizar
Para começar a usar o React, você precisará configurar um ambiente de desenvolvimento, incluindo Node.js e o gerenciador de pacotes npm ou yarn. Você pode criar um novo aplicativo React com a ferramenta create-react-app ou configurar manualmente seu projeto. Em seguida, você escreve seus componentes, define o estado e as propriedades, e o React cuida da renderização e atualização da interface do usuário de acordo com as mudanças nos componentes.

# Exemplo
No exemplo feito, temos um componente ListaDeItens que possui um estado para armazenar uma lista de itens e um novo item que o usuário pode adicionar. O método adicionarItem é chamado quando o botão "Adicionar Item" é clicado e atualiza o estado com o novo item. O método handleChange é usado para acompanhar as mudanças no campo de entrada de texto. A lista de itens é renderizada no elemento <ul>. o exemplo se encontra no módulo estudoReact.


