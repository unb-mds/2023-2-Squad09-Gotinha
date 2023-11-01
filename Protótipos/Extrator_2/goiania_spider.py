import scrapy
import datetime
from urllib.parse import urljoin
import subprocess
import re
import json


class GoianiaSpider(scrapy.Spider):
    TERRITORY_ID = '5208707'
    name = 'goiania_spider'
    alloy_domain = 'https://goiania.go.gov.br'
    start_url = ['https://www.goiania.go.gov.br/casa-civil/diario-oficial/']
    start_date = datetime.date(2023, 1, 1)

    def start_requests(self):
        year = 2023
        yield scrapy.Request(
            f"http://www.goiania.go.gov.br/shtml//portal/casacivil/lista_diarios.asp?ano={year}"
        )

    def parse(self, response):
        editions = response.xpath('*//a[@href]')

        for edition in editions[:6]:
            e_info = edition.xpath('./text()').get()

            num = re.search(r'Edi\u00e7\u00e3o  n\u00ba (\d+)', e_info).group(1)

            date = re.search(r'de (\d+ [^\d]+ \d+)', e_info).group(1)

            url = edition.xpath('./@href').get()
            full_url = urljoin(f"{self.alloy_domain}", url)
            
            sup = re.search(r'-\s+(.+)$', e_info)
            if sup:
                sup = "true"
            else:
                sup = "false"

            yield {
                'Edicao': num,
                'Data': date,
                'URL': full_url,
                'Suplemento': sup
            }


"""            
# Define o comando que você deseja executar no terminal pela IDE #
comando = "scrapy runspider goiania_api.py -o teste1.json"
resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE)
print(resultado.stdout.decode())
"""
