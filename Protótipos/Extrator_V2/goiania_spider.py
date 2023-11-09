import scrapy
import datetime
from urllib.parse import urljoin
import re


class GoianiaSpider(scrapy.Spider):
    # Identificador do território
    TERRITORY_ID = '5208707'

    # Nome do spider
    name = 'goiania_spider'

    # Domínio base
    alloy_domain = 'https://goiania.go.gov.br'

    # URL de início da raspagem
    start_url = ['https://www.goiania.go.gov.br/casa-civil/diario-oficial/']

    # Data de início
    start_date = datetime.date(2023, 1, 1)

    # Método para iniciar as requisições
    def start_requests(self):
        year = 2023
        # Cria uma requisição para o URL com base no ano
        yield scrapy.Request(
            f"http://www.goiania.go.gov.br/shtml//portal/casacivil/lista_diarios.asp?ano={year}"
        )

    # Método para processar as respostas das requisições
    def parse(self, response):
        editions = response.xpath('*//a[@href]')
        data_list = []  # Lista para armazenar os dados

        for edition in editions[:3]:
            e_info = edition.xpath('./text()').get()
            # Obtém a edição
            num = re.search(r'Edi\u00e7\u00e3o  n\u00ba (\d+)', e_info).group(1)
            # Obtém a data
            date = re.search(r'de (\d+ [^\d]+ \d+)', e_info).group(1)
            # Obtém a URL
            url = edition.xpath('./@href').get()
            full_url = urljoin(f"{self.alloy_domain}", url)
            # Verifica se é suplemento ou não
            sup = re.search(r'-\s+(.+)$', e_info)
            if sup:
                sup = "true"
            else:
                sup = "false"

            data_list.append({
                'Edicao': num,
                'Data': date,
                'URL': full_url,
                'Suplemento': sup
            })
    
        return data_list
        


"""            
execute o run.py para rodar o goiania_spider.py e o pdf_json.py
"""
