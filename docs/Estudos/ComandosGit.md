# Aprendizado Git #

## O que é o Git?

O Git é um sistema de controle de versão distribuído essencial no desenvolvimento de software, permitindo o rastreamento de mudanças em arquivos ao longo do tempo e facilitando o trabalho colaborativo em projetos. Neste guia, apresentaremos de forma clara e prática os principais comandos do Git, acompanhados de exemplos e descrições intuitivas, com o objetivo de tornar o aprendizado do Git mais acessível e compreensível.

## Comandos Essenciais do Git

Aqui estão os principais comandos do Git, explicados usando a metáfora de um álbum de fotos, juntamente com o que eles fazem no contexto do Git:

1. `git init` - (Inicialização do Álbum)

- **Descrição em Metáfora:** Imagine que você está prestes a criar um novo álbum de fotos. O `git init` é como abrir um novo álbum em branco e reservar espaço para todas as fotos que você planeja adicionar ao longo do tempo. É o começo do seu álbum de fotos.

- **No Git:** O comando `git init` cria um novo repositório Git no diretório atual, transformando-o em um espaço para rastrear alterações e versões de seus arquivos.

2. `git clone` - (Copiar um Álbum de Fotos)

- **Descrição em Metáfora:** Quando você deseja uma cópia completa de um álbum de fotos de um amigo, o `git clone` é como pedir a ele que copie todo o álbum para você. Você terá uma réplica idêntica em sua coleção.

- **No Git:** O comando `git clone` cria uma cópia idêntica de um repositório Git remoto em seu sistema local, permitindo que você colabore ou trabalhe em uma versão local do projeto.

3. `git branch` - (Ter Múltiplos Álbuns)

- **Descrição em Metáfora:** Você pode pensar no Git como uma coleção de álbuns. O `git branch` é como verificar quais álbuns estão disponíveis em sua coleção. Cada ramificação representa um álbum diferente para projetos distintos.

- **No Git:** O comando `git branch` lista todas as branches (ramificações) disponíveis no repositório, permitindo que você crie, altere e gerencie diferentes linhas de desenvolvimento.

4. `git checkout` - (Escolher um Álbum)

- **Descrição em Metáfora:** Quando você deseja trabalhar em um projeto específico, você "checa" esse álbum com o `git checkout`. É como escolher um álbum da sua coleção para começar a adicionar fotos ou fazer alterações.

- **No Git:** O comando `git checkout` permite que você mude para uma branch específica, permitindo que você trabalhe em diferentes partes do projeto ou em diferentes versões.

5. `git status` - (Verificar Fotos no Álbum)

- **Descrição em Metáfora:** O `git status` é como abrir seu álbum de fotos e verificar quais fotos já estão prontas para serem incluídas em uma página ou se algumas precisam ser organizadas melhor. Ele mostra o estado atual do álbum.

- **No Git:** O comando `git status` exibe informações sobre os arquivos no diretório de trabalho, mostrando quais foram modificados, quais estão na "staging area" e quais não estão sendo rastreados.

6. `git diff` - (Comparar Fotos)

- **Descrição em Metáfora:** Quando você deseja ver as diferenças entre duas fotos no álbum, o `git diff` é como pegar duas fotos, compará-las lado a lado e identificar as mudanças feitas entre elas.

- **No Git:** O comando `git diff` mostra as diferenças entre o que está no diretório de trabalho e o último commit, permitindo que você veja as alterações não registradas.

7. `git add` - (Adicionar Fotos ao Álbum)

- **Descrição em Metáfora:** O `git add` é como pegar fotos específicas e decidir que você deseja adicioná-las ao seu álbum. Você está colocando as fotos na "staging area", preparando-as para serem incluídas em uma página futura.

- **No Git:** O comando `git add` adiciona as mudanças dos arquivos ao índice (ou "staging area"), preparando-os para serem incluídos no próximo commit.

8. `git commit` - (Criar uma Página no Álbum)

- **Descrição em Metáfora:** Quando você adiciona várias fotos a uma página em seu álbum, você pode pensar no `git commit` como a criação dessa página. Você fornece uma mensagem para descrever o conteúdo da página e a salva no álbum.

- **No Git:** O comando `git commit` cria um novo commit com as mudanças na "staging area" e uma mensagem de commit que descreve as alterações feitas.

9. `git push` - (Compartilhar Fotos com Amigos)

- **Descrição em Metáfora:** O `git push` é como compartilhar suas fotos com amigos e familiares. Você está enviando suas fotos (ou seja, seus commits) para um álbum online ou para um local onde outras pessoas possam vê-las.

- **No Git:** O comando `git push` envia as mudanças do seu repositório local para o repositório remoto, permitindo que outros colaboradores acessem as alterações.

10. `git pull` - (Obter Fotos Atualizadas)

- **Descrição em Metáfora:** Quando seus amigos adicionam novas fotos ao álbum deles, o `git pull` é como pedir a eles para lhe fornecer as fotos mais recentes. Você atualiza seu álbum com as fotos mais recentes.

- **No Git:** O comando `git pull` obtém as mudanças do repositório remoto e as mescla com o seu repositório local, mantendo-o atualizado.

11. `git revert` - (Desfazer uma Edição)

- **Descrição em Metáfora:** Às vezes, você percebe que uma foto não ficou como você queria e deseja desfazer a edição. O `git revert` é como desfazer as alterações em uma foto específica e restaurá-la à versão anterior.

- **No Git:** O comando `git revert` cria um novo commit que desfaz as alterações feitas em um commit anterior, revertendo o estado do projeto para uma versão anterior.

12. `git merge` - (Combinar Fotos de Diferentes Álbuns)

- **Descrição em Metáfora:** Quando você tem fotos em dois álbuns diferentes e deseja combiná-las em um único álbum, o `git merge` é como pegar as fotos de ambos os álbuns e mesclá-las em um único álbum.

- **No Git:** O comando `git merge` combina as mudanças de uma branch em outra, permitindo que você integre o trabalho de diferentes linhas de desenvolvimento.

13. `git stash` - (Guardar Fotos Temporariamente)

- **Descrição em Metáfora:** Às vezes, você está trabalhando em uma página de álbum e precisa mudar para outra sem criar uma nova página. O `git stash` é como colocar temporariamente suas fotos em um armazenamento seguro para que você possa trabalhar em outra página e, em seguida, recuperar as fotos mais tarde.

- **No Git:** O comando `git stash` permite que você armazene temporariamente as mudanças não comprometidas, permitindo que você mude de branch ou aplique outras alterações sem fazer um commit.

## Links úteis:

[COMO USAR GIT E GITHUB NA PRÁTICA!](https://www.youtube.com/watch?v=UBAX-13g8OM)

[Comandos Git mais utilizados e como configurar](https://blog.geekhunter.com.br/comandos-git-mais-utilizados/)

[Comandos Git](https://comandosgit.github.io/)