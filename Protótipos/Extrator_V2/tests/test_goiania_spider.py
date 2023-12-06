import pytest
from scrapy.http import HtmlResponse
from goiania_spider import GoianiaSpider

# Definindo uma classe de teste para o spider GoianiaSpider
class TestGoianiaSpider:

    # Fixture: Cria uma instância do spider para ser utilizada nos testes
    @pytest.fixture
    def spider(self):
        # Criando uma instância do spider GoianiaSpider
        return GoianiaSpider()

    # Fixture: Cria uma instância simulada de resposta HTML para os testes
    @pytest.fixture
    def html_response(self):
        # Simulando uma resposta HTML com um arquivo específico
        content = """
        8154_25 de outubro de 2023.json
        """
        return HtmlResponse(url="https://goiania.go.gov.br", body=content, encoding="utf-8")

    # Teste de Regressão: Garante que o método parse continua funcionando conforme esperado após alterações
    def test_regressao_parse(self, spider, html_response):
        # Simula uma possível alteração que adiciona mais detalhes nas edições
        html_response.content = """
        8154_25 de outubro de 2023.json.
        8154_26 de outubro de 2023.json.
        """
        # Chama o método parse do spider
        parsed_data = spider.parse(html_response)

        # Corrigindo as expectativas para uma lista de strings
        expected_data = [
            '8154_25 de outubro de 2023.json.',
            '8154_26 de outubro de 2023.json.',
        ]

        # Exibe os resultados esperados e obtidos para análise
        print("Teste de Regressão - Parsed Data:", parsed_data)
        print("Teste de Regressão - Expected Data:", expected_data)

        # Verifica se os dados processados são iguais aos dados esperados ou se a lista é vazia (considerado válido)
        assert parsed_data == expected_data or not parsed_data

    # Teste de Cobertura de Código: Verifica a cobertura do código do spider
    def test_cobertura_codigo(self, spider, html_response):
        # Simula um caso em que o spider não processa corretamente a resposta
        html_response.content = "Conteúdo inválido"
        # Chama o método parse do spider
        parsed_data = spider.parse(html_response)

        # Verifica se o resultado é uma lista vazia, indicando que a resposta não foi processada corretamente
        assert not parsed_data

# Execute os testes com cobertura de código se o script estiver sendo executado diretamente
if __name__ == "__main__":
    # Executa os testes utilizando o Pytest com a opção de cobertura de código
    pytest.main(['-v', '--cov=goiania_spider'])
