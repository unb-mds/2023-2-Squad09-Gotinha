# Estudo do Git e GitHub 

<img src="https://github.com/unb-mds/2023-2-Squad09/blob/main/docs/Estudos/Imagens/Git%26GitHub.png" width="1000px" height="230px"/>

## Descrição Geral

* Arquivo criado para auxiliar no aprendizado e uso das ferramentas Git e GitHub. Pode ser utilizado em conjunto com o arquivo 
[Comandos Git](https://github.com/unb-mds/2023-2-Squad09/blob/main/docs/Estudos/ComandosGit.md), também desenvolvido por nós e presente neste repositório. 

## O que é o GitHub?

* De maneira resumida, o GitHub é uma plataforma totalmente online onde você pode criar repositórios e hospedar neles seus projetos, colaborar com softwares open source, seguir outros(as) programadores(as) e 
interagir com códigos de terceiros, entre outras funções, atualmente é a ferramenta mais popular utilizada para os fins citados, como uma espécie de "rede social para programadores".

## Criando e configurando um repositório no GitHub

* `Repositórios:` são os ambientes criados para armazenar seus códigos, imagens, documentações, entre outros arquivos relacionados ao seu projeto. Além disso, eles podem ser utilizados para 
trabalhar em equipe através de colaboradores, designação de tarefas para cada membro através das Issues, acompanhar os Insights do processo de desenvolvimento, etc;

* `Branch:` é o nome dado a uma versão (ramificação) do projeto. Isso é útil porque possibilita gerenciar múltiplas alterações acontecendo simultaneamente. Por exemplo, podemos fazer com que cada equipe de
desenvolvimento trabalhe em uma branch diferente;

* `Fork:` Quando um desenvolvedor precisa começar a trabalhar em um projeto, seu primeiro passo é copiar este repositório para a sua máquina, este processo é realizado pelo comando fork. O fork também é uma
funcionalidade útil quando um membro da equipe precisa pegar um código público para manuseá-lo em um editor de código local ou interno.

* Confira abaixo algumas das possibilidades:

#### 1. Criando um novo repositório:
![1](https://github.com/unb-mds/2023-2-Squad09/blob/main/docs/Estudos/Imagens/Criando%20Reposit%C3%B3rio%201.png)
<br/>

#### 2. Configurando o nome, privacidade, licença, entre outras coisas:
![2](https://github.com/unb-mds/2023-2-Squad09/blob/main/docs/Estudos/Imagens/Configurando%20Reposit%C3%B3rio%202.png)
<br/>

#### 3. Aqui você pode escolher adquirir o GitHub Copilot, convidar colaboradores, copiar o link do repositório, adicionar o(s) primeiro(s) arquivo(s) e vizualizar a lista dos principais comandos do Git:
![3](https://github.com/unb-mds/2023-2-Squad09/blob/main/docs/Estudos/Imagens/Configura%C3%A7%C3%B5es%20e%20Comandos%203.png)
<br/>

#### 4. Página inicial do repositório ao adicionar o primeiro arquivo, na parte superior, é possível navegar entre as diferentes funções. Na direita, você pode adicionar novos arquivos manualmente. Abaixo de name, você pode vizualizar a lista de arquivos ali presentes, um pouco pra cima é possível ver a branch atual (main no caso):
![4](https://github.com/unb-mds/2023-2-Squad09/blob/main/docs/Estudos/Imagens/Tela%20Inicial%20do%20Reposit%C3%B3rio%204.png)
<br/>

#### 5. Ao clicar no botão da branch atual (no caso a main), é possível vizualizar todas as branchs e tags do repositório atual:
![5](https://github.com/unb-mds/2023-2-Squad09/blob/main/docs/Estudos/Imagens/Branch%201.png)
<br/>

#### 6. Nesta tela você pode modificar, excluir ou criar uma nova branch clicando em "New branch", agora basta nomear a branch e escolher de onde ela irá "herdar" os arquivos e confirmar.
![6](https://github.com/unb-mds/2023-2-Squad09/blob/main/docs/Estudos/Imagens/New%20Branch%202.png)
<br/>

#### 7. Outra possibilidade é a [Clonagem](https://docs.github.com/pt/get-started/getting-started-with-git/about-remote-repositories) de um repositório, você pode clonar no Git através da URL ou simplesmente baixar o repositório completo em um arquivo compactado .zip.
![7](https://github.com/unb-mds/2023-2-Squad09/blob/main/docs/Estudos/Imagens/Git%20Clone.png)
<br/>

#### 8. Existem duas formas de você salvar um repositório de outra pessoa no seu perfil. A primeira é fazendo um fork, no qual nessa opção o repositório escolhido aparecerá no seu perfil e você poderá fazer alterações e contribuir para o projeto principal criando a sua própria branch. A segunda opção é apenas marcando como favorito para que ele fique salvo no seu perfil (sem fazer nenhuma alteração).
![8](https://github.com/unb-mds/2023-2-Squad09/blob/main/docs/Estudos/Imagens/Fork%201.png)
<br/>

## Informações Adicionais 

* Git e GitHub normalmente aparecem em conjunto, mas não são a mesma coisa; 

* O Git foi criado em 2005, é um sistema de versionamento de código distribuído e foi criado por Linus Torvalds (criador do Linux e do Git); 

* Apesar de serem o sistema / plataforma mais popular hoje em dia, existem outras que também realizam funções semelhantes, como por exemplo BitKeeper, CVS, GitLab, Bitbucket, entre outras; 

* Algumas vantagens do uso da tecnologia do Git e GitHub:
  - Aprender a programar; <br/>
  - Controle de versão; <br/> 
  - Armazenamento em nuvem; <br/> 
  - Trabalhar em equipe; <br/>
  - Melhorar o seu projeto através da comunidade; <br/>
  - Reconhecimento através do seu portifólio. <br/>
  - Entre outras...

## Comandos complementares do git: 

`git log` ---> Mostra os logs de commit;

`git remote add <origin> <link do repositório.git>` ---> Estabelece a conexão entre a máquina local e o repositório remoto;

`git update-git-for-windows` ---> Atualiza o git para a versão mais recente; 

`git version` ---> Exibe a versão git atualmente instalada;

`git help` ---> Exibe os principais comandos com uma breve descrição; 

`git help git` ---> Abre a página de manual (git(1) Manual Page).

* Existem outros diversos comandos e subcomandos que são mais específicos, e portanto, menos utilizados.

 * Usuários do Windows utilizam um terminal derivado do Shell (CMD), e usuários de sistemas operacionais derivados do Unix (Linux, Mac OS, etc) utilizam um terminal derivado do Bash, ou seja,
 muitos conjuntos de comandos são diferentes ao utilizar diferentes tipos de terminais, especialmente ao manipular arquivos. 

## Links Úteis

* [Documentação GitHub Docs](https://docs.github.com/pt) <br/> 
* [Documentação mais recente do Git](https://git-scm.com/docs) <br/>
* [Lista de comandos úteis do GIT](https://gist.github.com/leocomelli/2545add34e4fec21ec16) <br/>
* [Sobre repositórios remotos](https://docs.github.com/pt/get-started/getting-started-with-git/about-remote-repositories)
