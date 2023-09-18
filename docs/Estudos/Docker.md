# Introdução ao Docker

## O que é o Docker?
O Docker é uma plataforma de código aberto que simplifica a criação, distribuição e execução de aplicativos em contêineres. Um contêiner é uma unidade leve e independente que inclui todo o ambiente necessário para executar um aplicativo, como código, bibliotecas e dependências.


Docker não é uma virtualização: O Docker não utiliza virtualização tradicional; em vez disso, isola aplicativos em contêineres leves.

Engine de administração de containers: O Docker é uma plataforma para criar, executar e gerenciar contêineres.

Container = "Sistema de arquivos" + "DAEMON (processo)": Um contêiner Docker consiste em um sistema de arquivos e um processo isolado.

Criado em linguagem "GO" (Google) baseado em sistemas Linux (LXC): O Docker foi desenvolvido em Go e baseado em tecnologias Linux.

Containers são gerados a partir de imagens: Os contêineres são instâncias de imagens que incluem recursos para executar aplicativos.

Docker Registry: O Docker Hub fornece uma biblioteca de imagens pré-construídas para uso gratuito.

## Principais Vantagens do Docker
- **Isolamento:** Os contêineres oferecem isolamento completo entre aplicativos, garantindo que eles não interfiram uns com os outros.
- **Portabilidade:** Os contêineres podem ser executados em qualquer lugar, desde laptops até servidores de produção e ambientes de nuvem.
- **Eficiência:** O Docker é eficiente em termos de recursos, permitindo que você execute mais aplicativos em um único servidor.
- **Escalabilidade:** Os contêineres podem ser facilmente dimensionados horizontalmente para lidar com cargas de trabalho variáveis.

# Conceitos Fundamentais

## Imagem Docker
Uma imagem Docker é um pacote de leitura apenas que contém um sistema de arquivos com código e dependências do aplicativo. Ela é uma representação estática de um ambiente de aplicativo.

## Contêiner Docker
Um contêiner Docker é uma instância em execução de uma imagem Docker. Ele é isolado do sistema host e pode ser executado e implantado de forma independente. Os contêineres são a unidade de execução do Docker.

## Dockerfile
Um Dockerfile é um arquivo de configuração que define como construir uma imagem Docker. Ele especifica as instruções para copiar arquivos, instalar dependências e configurar o ambiente do aplicativo. É a receita para criar uma imagem.

## Docker Compose
O Docker Compose é uma ferramenta que permite definir e executar aplicativos multi-contêiner em um único arquivo de configuração. Ele facilita a orquestração de contêineres relacionados.

# Instalação do Docker
Para começar a usar o Docker, é necessário instalá-lo na sua máquina. As instruções específicas para a sua plataforma podem ser encontradas no [site oficial do Docker](https://docs.docker.com/).

# Comandos Básicos do Docker
Aqui estão alguns comandos essenciais do Docker para começar:

- `docker pull <imagem>`: Baixa uma imagem Docker do Docker Hub ou de um registro personalizado.
- `docker run <imagem>`: Executa um contêiner com base em uma imagem.
- `docker ps`: Lista os contêineres em execução.
- `docker stop <contêiner>`: Para um contêiner em execução.
- `docker build -t <nome_da_imagem> <caminho_do_Dockerfile>`: Cria uma imagem Docker a partir de um Dockerfile.
- `docker-compose up`: Inicia aplicativos multi-contêiner definidos no Docker Compose.

# Exemplos de Uso

## Executando um Contêiner de Exemplo
```shell
docker run -d --name meu-contêiner nginx

Este comando inicia um contêiner Nginx em segundo plano.

docker run: Este é o comando principal para executar um contêiner a partir de uma imagem.

-d: Esta opção indica que o contêiner deve ser executado em segundo plano, ou seja, ele não irá bloquear a janela de terminal atual. É comumente usada para aplicativos que precisam ser executados como serviços em segundo plano.

--name meu-contêiner: Aqui, você está atribuindo um nome ao seu contêiner, que neste caso é "meu-contêiner". Isso é útil para que você possa se referir facilmente ao contêiner posteriormente por esse nome.

nginx: Isso especifica a imagem que será usada para criar o contêiner. Neste caso, estamos usando a imagem oficial do Nginx, um servidor web popular.

Em resumo, o comando acima inicia um contêiner chamado "meu-contêiner" baseado na imagem do Nginx e o executa em segundo plano como um servidor web. Você pode acessar o servidor Nginx no contêiner através do navegador ou fazer outras operações relacionadas a esse contêiner, como pará-lo ou verificar seu status.

# Conclusão
O Docker oferece a flexibilidade de criar imagens personalizadas para seus aplicativos, permitindo que você configure o ambiente de acordo com suas necessidades específicas. Isso torna o Docker uma ferramenta valiosa para desenvolvedores e operadores que desejam garantir a consistência e a portabilidade de seus aplicativos em diferentes ambientes.

Para aprender mais sobre a criação de imagens Docker personalizadas e explorar recursos avançados, consulte a documentação oficial do Docker (https://docs.docker.com/). 
