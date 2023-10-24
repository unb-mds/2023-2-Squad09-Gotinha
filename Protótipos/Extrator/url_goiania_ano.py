import scrapy
import datetime
from urllib.parse import urljoin


class GoianiaSpider(scrapy.Spider):
    TERRITORY_ID = '5208707'
    name = 'goiania_spider'
    alloy_domain = 'https://goiania.go.gov.br'
    start_url = ['https://www.goiania.go.gov.br/casa-civil/diario-oficial/']
    # Reduzir o ano inicial de 1960 para 2000:
    start_date = datetime.date(2000, 1, 1)

    def start_requests(self):
        # Aqui, deverá ser modificado para receber a requisição do usuário:
        year = 2023
        # Solicitação scrapy para o ano selecionado
        yield scrapy.Request(
            # f-string para construir a URL da página que deseja raspar, com base no ano
            f"http://www.goiania.go.gov.br/shtml//portal/casacivil/lista_diarios.asp?ano={year}"
        )

    def parse(self, response):
        editions = response.xpath('*//a[@href]')

        for edition in editions:
            url = edition.xpath('./@href').get()
            full_url = urljoin(f"{self.alloy_domain}", url)
            yield {
                'url': full_url
            }


"""
Para executar, primeiro navegue pelo terminal até o diretório onde este código está localizado.
Feito isso, basta executar o seguinte comando: scrapy runspider nome_arquivo.py -o arquivo_extraído.extensão
A extensão de saída pode ser: json, jsonlines, jsonl, jl, csv, xml, marshal ou pickle.
"""
