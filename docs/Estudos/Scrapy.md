# Scrapy e suas funcionalidades pelo terminal

<p align="center"> <img src="https://github.com/unb-mds/2023-2-Squad09/blob/main/docs/Estudos/Imagens/Scrapy.png" width="750px" height="250px"/> </p>

* Scrapy é um framework/biblioteca de código aberto desenvolvido em Python e mantido pela Zyte (empresa especializada em extração de dados) e vários outros colaboradores. Essa ferramenta é utilizada para extrair dados de sites, de forma rápida simples e extensível, utilizando métodos conhecidos como web-scraping, web-crawling, raspagem, entre outros.

## Instalação e configuração do ambiente  

**1. Instale o Python:** para utilizar o Scrapy, antes, é necessário ter instalado a versão mais recente do Python.

* Para instalar, é necessário fazer o download do instalador executável mais recente e compatível com a sua máquina e executá-lo (lembre-se de colocar o PATH incluso para permitir manipulações pelo terminal). Feito isso, verifique se a instalação foi concluída com sucesso pelo terminal:

`python --version` --> Exibe a versão do Python instalada

`python` --> Exibe a versão do Python instalada com mais detalhes, além de permitir que os comando em Python sejam executados.

**2. Instale o Scrapy:**

* Para instalar a última versão do Scrapy, digite o seguinte comando no terminal: `pip install scrapy` 

* Para verificar se a última versão foi instalada com sucesso digite:
```python
python #Inicializa o Python

import scrapy #Importa a biblioteca Scrapy

print (scrapy.__version__) #Exibe a versão instalada
```

**3. Instale o pip (ou semelhante) :** pip é um sistema de gerenciamento de pacotes padrão usado para instalar e gerenciar pacotes de software escritos em Python.

* Primeiro verifique se em sua máquina já existe a versão mais recente pip, pois algumas distribuições do python já vem com o pip pré-instalado, no terminal, digite: `pip --version`.

* Caso não esteja instalado, ou desatualizado, é possível instalar ou atualizar de 2 formas: 

1. `pip install pip` --> Instala a última versão.

2. `pip install pip==<versão do pip desejada>` --> Nesse caso é possível escolher diretamente qualquer versão.

## Exemplo de Scraping com o site ["Quotes to Scrape"](https://quotes.toscrape.com/) pelo terminal:

1. `scrapy shell https://quotes.toscrape.com/` --> Requisição de uma página usando o Scrapy, será gerado um arquivo de log e um arquivo response.

* Feito isso, existe duas formas de extrair os dados de uma página web, usando o `response.xpath` ou `response.css`(são seletores utilizados para navegar por documentos que usam marcadores) .

* Para começar, devemos entender a estrutura da página web em que vamos extrair os dados, isso pode ser feito através da ferramenta inspecionar elemento (Ctrl+Shift+C (Windows, Linux) ou Command+Shift+C (macOS)).

### **Alguns comandos essenciais que podem ser utilizados para acessar os dados:**

2. `response.xpath("*//div")` --> Escolhe a estrutura para acessar, com esse comando, todas as "divs" são exibidas.

3. `response.xpath("*//div/span")` --> Exibe todos os "spans" (agrupamentos de elementos).

* Para acessar os dados, é preciso ser mais específico. Primeiramente, vamos extrair todos os textos/frases:

4. `response.xpath("*//div/span[@class='text']\text()").getall()` --> Como agora vamos acessar um elemento, precisamos colocar `[@class='<nome da classe']/text()` e `.getall()` para extair os dados no formato de texto. Será exibido todos os textos presentes na página.

5. `len(response.xpath("*//small[@class='author']/text()").getall())` --> O comando `len` exibe o número de elementos encontrados, nesse caso, o número de textos/frases. Utilizado para realizar a contagem ou verificar se o número corresponde.

* Agora, queremos extrair todos os autores:

6. `response.xpath("*//small[@class='author']/text()").getall()` --> O mesmo comando, porém estamos acessando a classe "author". Será exibido todos os autores.

* Para acessar apenas um elemento específico, pode-se copiar o endereço XPath. Exemplo:

<p align="center"> <img src="https://github.com/unb-mds/2023-2-Squad09/blob/main/docs/Estudos/Imagens/Copy%20XPath.png"/> </p>

7. `response.xpath("/html/body/div/div[2]/div[1]/div[1]/span[1]/text()").getall()` --> Na saída será exibido o texto/frase especificado.

* Todos essas funções são possíveis utilizando o `response.css`, porém com uma sintaxe um pouco diferente. Foi demonstrado utilizando o `response.xpath` pois ele é mais abrangente e robusto.
 
8. `response.css('a.tag::text').getall()` --> Exemplo de extração de todas as tags da página web com `response.css`.

## Links Úteis

* [Exemplo de Scrapy](Scrapy2.md)
* [Minicurso Web Scrapy com Python | Scrapy](https://www.youtube.com/watch?v=nyn0IIjoc_o&list=PLcgrCjGCdYEJZDPfsI06YuvbGIApsk7ZB&ab_channel=SynapseDataScience) </br>
* [Site da Empresa - Zyte](https://www.zyte.com/access-web-data/) </br>
* [Site Oficial - Scrapy](https://scrapy.org/) </br>
* [Documentação - Scrapy 2.11](https://docs.scrapy.org/en/latest/)</br>
