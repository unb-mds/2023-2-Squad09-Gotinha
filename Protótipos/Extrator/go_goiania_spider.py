import scrapy
import datetime
from urllib.parse import urljoin


class GoianiaSpider(scrapy.Spider):
    TERRITORY_ID = '5208707'
    name = 'goiania_spider'
    alloy_domain = 'https://goiania.go.gov.br'
    start_url = ['https://www.goiania.go.gov.br/casa-civil/diario-oficial/']
    start_date = datetime.date(1960, 4, 21)

    def start_requests(self):
        initial_year = self.start_date.year
        end_year = datetime.date.today().year
        for year in range(initial_year, end_year + 1):
            yield scrapy.Request(
                f"http://www.goiania.go.gov.br/shtml//portal/casacivil/lista_diarios.asp?ano={year}"
            )

    def parse(self, response):
        editions = response.xpath('*//a[@href]')

        for edition in editions:
            url = edition.xpath('./@href').get()
            full_url = urljoin(f"{self.alloy_domain}", url)
            yield {
                'edition_info': edition.xpath('./text()').get(),
                'url': full_url
            }
