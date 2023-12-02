# Extrator

- Extrair os diários oficiais e armazenar.
- Extrair os decretos orçamentários que envolva a área da saúde.
- Armazenar os dados extraidos.

## Ambiente virtual:

- Somente para caso não esteja funcionando.
- Baixe os arquivos [setup.sh](https://github.com/unb-mds/2023-2-Squad09-Gotinha/blob/main/Protótipos/Extrator_V2/setup.sh) e [requirements.txt](https://github.com/unb-mds/2023-2-Squad09-Gotinha/blob/main/Protótipos/Extrator_V2/requirements.txt).
- Adicione esses dois arquivos ao diretório do extrator.
- navegue pelo terminal até o diretório e execute

```
chmod +x setup.sh 
```
```
./setup.sh
```

- Siga as instruções que aparecerão.

# goiania_spider.py

- 
- Pega as url, data, edição e se tem suplemento ou não. E armazena esses dados em um json.
- Precisa ser executado separadamente e antes da run.
- Lembre-se de navegar pelo terminal até o diretório onde está localizado o arquivo goiania_spider.py
- Execute "scrapy runspider goiania_spider.py -o edicoes_recentes_ano.json" sendo o ano que vai ser extraido.

```
 # Domínio base
    alloy_domain = 'https://goiania.go.gov.br'

    # URL de início da raspagem
    start_url = ['https://www.goiania.go.gov.br/casa-civil/diario-oficial/']

    # Data de início
    start_date = datetime.date(2022, 1, 1)

    # Método para iniciar as requisições
    def start_requests(self):
        year = 2022
        # Cria uma requisição para o URL com base no ano
        yield scrapy.Request(
            f"http://www.goiania.go.gov.br/shtml//portal/casacivil/lista_diarios.asp?ano={year}"
        )
```

- Modicifando essa parte para mudar o município e o ano desejado.

# Run

- Depois de terminar de roda o goiania_spider execute o run pela própria IDE (se tiver).
- O run irá baixar os diários oficias no formato json dentro de uma pasta "Diários em json/diarios_2023" por exemplo.
- Em seguida irá mandar esses diários para [filtro.py](https://github.com/unb-mds/2023-2-Squad09-Gotinha/blob/main/Protótipos/Extrator_V2/filtro.py) onde irá busca os decretos orçamentários sobre a área da saúde e armazenar as iformações de todos os diários no [trechos_filtrados.json](https://github.com/unb-mds/2023-2-Squad09-Gotinha/blob/main/Protótipos/Extrator_V2/trechos_filtrados.json).


## Resultados

```
[
 {"Decreto Nº": "02", "Mês": 1, "Ano": "2023", "Órgão": "Secretaria Municipal de Saúde –\nFundo Municipal de Saúde", "Valor em R$": 9000000.0},
 {"Decreto Nº": "08", "Mês": 1, "Ano": "2023", "Órgão": "Ins  tuto Municipal de\nAssistência à Saúde dos Servidores de Goiânia", "Valor em R$": 30000000.0},
 {"Decreto Nº": "09", "Mês": 1, "Ano": "2023", "Órgão": "Secretaria Municipal de Saúde –\nFundo Municipal de Saúde", "Valor em R$": 20000000.0},
 {"Decreto Nº": "39", "Mês": 2, "Ano": "2023", "Órgão": "Secretaria Municipal de\nSaúde – Fundo Municipal de Saúde", "Valor em R$": 8500000.0},
]
```
