import datetime
import re
import scrapy

from dateparser import parse
from data_collection.gazette.items import Gazette
from data_collection.gazette.spiders.base.__init__ import BaseGazetteSpider


class GoAnapoliSpider(BaseGazetteSpider):
    name = "go_anapolis"
    TERRITORY_ID = "5201108"
    allowed_domains = ["anapolis.go.gov.br"]
    start_urls = ["https://dom.anapolis.go.gov.br/"]
    start_date = datetime.date(2019, 3, 1)

    def parse(self, response):
        initial_year = self.start_date.year
        end_year = datetime.date.today().year

        for year in range(initial_year, end_year + 1):
            for month in range(1, 12):
                yield scrapy.Request(f"https://dom.anapolis.go.gov.br/api/diarios/diariosPorDia?data={year}-{month}")
                for dia in range(1, 31):
                    if dia != " ":
                        yield scrapy.Request(
                            f"https://dom.anapolis.go.gov.br/api/diarios?data={year}-{month}-{dia}&calendar=true&situacao=2")
                        gazette_idd = idd
                        gazette_edition = numero
                        gazette_date = parse(f"{dia} de {month} de {year}", languages=["pt"]).date()
                        gazette_file_name = file_name
                        gazette_url1 = f"https://diariooficial.s3.us-east-2.amazonaws.com/cliente/pf_anapolis/legacy/{gazette_file_name}.pdf"
                        gazette_url2 = f"https://diariooficial.s3.us-east-2.amazonaws.com/cliente/pf_anapolis/{gazette_idd}/{gazette_file_name}.pdf"

                        yield Gazette(
                            date=gazette_date,
                            edition_number=gazette_edition,
                            file_urls1=[gazette_url1],
                            file_urls2=[gazette_url2],
                            is_extra_edition=False,
                            power="executive",
                        )
