# Importa o scrapy
import scrapy
# Importa o módulo datetime, para manipulação de datas e horas
import datetime
# Importa a função urljoin do módulo urllib.parse, para combinar/unir URLs.
from urllib.parse import urljoin


# Estrutura da spider
class GoianiaSpider(scrapy.Spider):
    # Código do IBGE para Goiânia:
    TERRITORY_ID = '5208707'
    # Nome da spider:
    name = 'goiania_spider'
    # Domínio do site:
    alloy_domain = 'https://goiania.go.gov.br'
    # Diários separados p/ano:
    start_url = ['https://www.goiania.go.gov.br/casa-civil/diario-oficial/']
    # Data da primeira publicação:
    start_date = datetime.date(1960, 4, 21)

    # Define um método para iniciar as solicitações de busca da spider
    def start_requests(self):
        # Obtém o ano da primeira publicação
        initial_year = self.start_date.year
        # Obtém o ano da última (ou ano atual) publicação
        end_year = datetime.date.today().year
        # Loop para percorrer por cada ano
        for year in range(initial_year, end_year + 1):
            # Solicitação scrapy para cada ano
            yield scrapy.Request(
                # f-string para construir a URL da página que deseja raspar, com base no ano
                f"http://www.goiania.go.gov.br/shtml//portal/casacivil/lista_diarios.asp?ano={year}"
            )

    # Define o método parse para processar a resposta da solicitação feita acima
    def parse(self, response):
        # Extrai todos os elementos <a> que possuem um atributo href
        editions = response.xpath('*//a[@href]')

        # Loop para buscar todos os links
        for edition in editions:
            # Extrai o valor do atributo href, no caso, a segunda parte da URL do arquivo
            url = edition.xpath('./@href').get()
            # Usa a função urljoin para unir o domínio da spider a URL obtida logo acima
            full_url = urljoin(f"{self.alloy_domain}", url)
            # Cria um dicionário contendo:
            yield {
                # Informações sobre a edição (número e data da publicação)
                'edition_info': edition.xpath('./text()').get(),
                # URL completa
                'url': full_url
            }


"""
Para executar, primeiro navegue pelo terminal até o diretório onde este código está localizado.
Feito isso, basta executar o seguinte comando: scrapy runspider <go_goiania_spider.py> -o <arquivos_extraídos.extensão>
A extensão de saída pode ser: json, jsonlines, jsonl, jl, csv, xml, marshal ou pickle.
"""
