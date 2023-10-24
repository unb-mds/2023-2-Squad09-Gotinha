# Raspagem do site ["Quotes to Scrape"](https://quotes.toscrape.com/)

## Descrição Geral

* Este arquivo é uma continuação do arquivo sobre [Scrapy e suas funcionalidades](https://github.com/unb-mds/2023-2-Squad09/blob/main/docs/Estudos/Scrapy1.md), em que aprendamos a instalar e configurar o ambiente de trabalho e aprendemos também, como navegar, acessar e obter informações de uma página web pelo terminal. É recomendado a leitura prévia.

* O site ["Quotes to Scrape"](https://quotes.toscrape.com/) é uma página web simples criada para treinar webscraping, nela contém citações, no qual cada citação possui um texto/frase, um autor e uma ou mais tags associadas.

* No diretório [Raspagem 'Quotes to Scrape'](https://github.com/unb-mds/2023-2-Squad09/tree/main/Prot%C3%B3tipos/Raspagem%20'Quotes%20to%20Scrape'), fizemos uma implentação em código da raspagem e exportamos para dois arquivos-exemplos (.json e .csv).

* Abaixo vamos explicar o conceito de "Spider", com alguns exemplos das aplicações práticas no site em questão, além de explicar um pouco sobre formatos de arquivos.

## O que é Spider?

* Uma parte fundamental do framework Scrapy, é o conceito de "spider (aranha)". Basicamente, spider é um programa em Python que define como o Scrapy deve acessar e raspar uma página web específica. As spiders são responsáveis por:

**1. Definir as URLs iniciais:** As spiders começam a navegar em um site a partir de URLs específicas, chamadas de "URLs iniciais". Essas URLs podem ser fornecidas manualmente na spider ou geradas dinamicamente.

**No código:**
```python
start_urls = ['https://quotes.toscrape.com/']
```

**2. Fazer solicitações HTTP:** As spiders fazem solicitações HTTP para as URLs iniciais e outras páginas do site para obter o conteúdo da web.
```python
class QuotesSpider(scrapy.Spider):
  name = 'QuotesSpider'
  start_urls = ['https://quotes.toscrape.com/'] 
```

**3. Processar as respostas:** Após receber as respostas das solicitações HTTP, as spiders processam o conteúdo da página para extrair os dados desejados. Isso geralmente envolve o uso de expressões XPath ou seletores CSS para localizar elementos HTML específicos que contenham os dados de interesse.

**No código:**
```python
def parse(self, response):
  quotes = response.xpath('*//div[@class="quote"]')
  for q in quotes:
        yield {
        'text': q.xpath('.//span[@class="text"]/text()').get(),
        'author': q.xpath('.//small[@class="author"]/text()').get(),
        'tags': q.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall() 
        } # Dicionário {text, author, tags}
```

**4. Seguir links:** As spiders podem seguir links para outras páginas dentro do site, permitindo que coletem informações de várias páginas.

**No código:**
```python
next_page = response.xpath('*//li[@class="next"]/a/@href').get()

if next_page is not None:
  yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
# Trecho também aplicável aos tópicos 6 e 7 abaixo.
```

**5. Armazenar os dados:** Os dados extraídos são geralmente armazenados em um formato estruturado, como JSON ou CSV, ou podem ser enviados para um banco de dados para análise posterior.

**No terminal:**
`scrapy runspider Scrapy_Quotes.py -o Teste.json` ---> Sintaxe Básica: scrapy runspider <Nome do código.py> -o <Nome do arquivo.extensão>

**6. Gerenciar estados:** As spiders podem gerenciar estados para evitar o acesso repetido a páginas já visitadas e garantir que todas as páginas relevantes sejam processadas.

**7. Tratamento de erros:** As spiders podem ser configuradas para lidar com erros, como páginas não encontradas ou bloqueios do servidor, de maneira apropriada.

* Observação: o código completo e comentado se encontra no diretório citado na descrição geral.

* As spiders são altamente configuráveis e personalizáveis, permitindo que você adapte a lógica de raspagem para atender às necessidades específicas do site que está sendo raspado. Cada spider é uma classe Python que herda funcionalidades do Scrapy e implementa métodos específicos, como parse, para definir o comportamento da spider. Em essência, as spiders são uma maneira eficaz e poderosa de automatizar a coleta de dados da web de forma estruturada.

## Por que trabalhar com arquivos .json e/ou .csv?

* Exportar dados raspados de um site para um arquivo .json ou .csv oferece várias vantagens, veja abaixo algumas delas:

**`1. Estrutura de dados organizada:`** Ambos são formatos estruturados que permitem organizar os dados de uma maneira legível e lógica. Isso facilita a leitura, escrita, controle, análise e o processamento posterior dos dados.

**`2. Portabilidade:`** Arquivos .json e .csv são formatos de dados amplamente suportados por várias linguagens de programação, bancos de dados e aplicativos. Isso significa que você pode facilmente importar e exportar esses dados para outras pessoas, utilizando diferentes sistemas e ferramentas.

**`3. Compatibilidade com planilhas:`** Arquivos CSV podem ser abertos diretamente em aplicativos de planilha, como o Microsoft Excel e o Google Sheets. Isso facilita a visualização e a análise dos dados em um formato familiar.

**`4. Tamanho de arquivo menor:`** Comparados a outros formatos, como HTML ou XML, tanto o .json quanto o .csv tende a ser mais compacto, economizando espaço de armazenamento e tempo ao transferir os dados.

**`5. Suporte a estrutura de dados complexa:`** Se os dados que você está raspando têm uma estrutura complexa com aninhamento de objetos e arrays, o JSON é especialmente útil para representar esses dados de forma hierárquica.

**`6. Preservação de tipos de dados:`** Ambos permitem que você mantenha informações sobre os tipos de dados dos campos, como números, datas e texto, facilitando a análise subsequente.

**`7. Integração com APIs e bancos de dados:`** Geralmente são mais fáceis para importar dados em sistemas de banco de dados ou em serviços de API, tornando-os úteis para alimentar outras partes do seu aplicativo ou pipeline de dados.

* No entanto, é importante observar que a escolha entre JSON e CSV depende das suas necessidades específicas. O JSON é mais adequado para dados complexos com estruturas aninhadas, enquanto o CSV é mais simples e amplamente compatível, tornando-o uma escolha sólida para dados tabulares. A escolha também pode depender das ferramentas e linguagens de programação que você planeja usar para manipular esses dados.
