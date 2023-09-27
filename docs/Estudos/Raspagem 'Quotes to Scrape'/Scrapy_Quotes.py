# 1. Importa a biblioteca Scrapy.
import scrapy                                                                           

# 2. Cria uma Spider class.
class QuotesSpider(scrapy.Spider):
    # 3. Define o nome da spider.
    name = 'QuotesSpider'
    # 4. Indica a URL em que serão feitas as requisições.
    start_urls = ['https://quotes.toscrape.com/']                                        

    # 5. Método parse para processar as solicitações HTTP.
    def parse(self, response):
        # 6. Extrai todos os elementos HTML do endereço citado.
        quotes = response.xpath('*//div[@class="quote"]')
        # 7. Laço de repetição para navegar entre os elementos.
        for q in quotes:
                # 8. Método para retornar um dicionário contendo as informações extraídas.
                yield {
                # 9. Extrai o texto da citação.
                'text': q.xpath('.//span[@class="text"]/text()').get(),
                # 10. Extrai o autor da citação.
                'author': q.xpath('.//small[@class="author"]/text()').get(),
                # 11. Extrai as tags associadas à citação.
                'tags': q.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall() 
                }
          
        # 12. Extrai o botão next.
        next_page = response.xpath('*//li[@class="next"]/a/@href').get()        
      
        # 13. Verifica se a próxima página é nula/vazia:
        if next_page is not None:
            # 14. Cria uma nova request, chama o método parse novamente.
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)       
          
# 15. Para exportar os dados para algum arquivo (json, jsonlines, jsonl, jl, csv, xml, marshal ou pickle) digite no terminal: scrapy runspider <Nome do script.py> -o <Nome do arquivo.extensão>
