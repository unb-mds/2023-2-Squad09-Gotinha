import scrapy
import datetime
from urllib.parse import urljoin
import re


class LuzianiaSpider(scrapy.Spider):
    # Identificador do território
    TERRITORY_ID = '5212501'

    # Nome do spider
    name = 'luziania_spider'

    # Domínio base
    alloy_domain = 'https://www.luziania.go.gov.br/'

    # URL de início da raspagem
    start_url = ['https://www.luziania.go.gov.br/decretos-orcamentarios-2021']

    # Método para iniciar as requisições
    def start_requests(self):
        year = 2023
        page_num = 1
        max_pages = 10
        
        while page_num <= max_pages:
            url = f"https://www.luziania.go.gov.br/decretos-orcamentarios-2021/jsf/jet-engine/pagenum/{page_num}/search/{year}/"
            yield scrapy.Request(url, callback=self.parse)
            
            # Incrementa o número da página para a próxima iteração
            page_num += 1
            
    # Método para processar as respostas das requisições
    def parse(self, response):
        decretos = response.xpath('/html/body/div/div/main/div/section/div/div/div/div/div/div/div/div/div')
        
        data_list = []
        
        for decreto in decretos:
            dados = decreto.xpath('.//section[1]/div/div/div/div/div/h2/a/text()').get()
            
            # Obtém a edição
            num_match = re.search(r'\u00c1RIO N\u00ba (\d+)', dados)
            num = num_match.group(1) if num_match else None
        
            # Obtém a data
            data_match = re.search(r'de (\d+ [^\d]+ \d+)', dados, re.IGNORECASE)
            data = data_match.group(1) if data_match else None
            
            # Obtém a URL
            link = decreto.xpath('.//section[3]/div/div/div/div/div/div/div/div/div/a[1]/@href').get()
                
            data_list.append({
                'Decreto': num,
                'Data': data,
                'URL': link
            })
    
        return data_list