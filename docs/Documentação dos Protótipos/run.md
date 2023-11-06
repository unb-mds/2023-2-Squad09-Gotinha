# Unindo o spider com o pdf para json

- A ideia é fazer rodar os dois com um click.
- Gerando o arquivo .json que contenha edição, ano, link e se é suplemento.
- A outra parte gerando uma pasta com os diários oficiais selecionados pelo arquivo de cima.
- Com esses resultados conseguimos então utilizar o elasticsearch para filtrar e buscar exatamente o que desejamos nos diários oficiais.

## Ambiente virtual:

- Foi necessário criar um ambiente virtual para conseguir rodar todos unidos.
- Para isso abra o terminal e digite o seguinte comando para criar um ambiente virtual:

```

python3 -m venv nome_do_ambiente
```

Substitua nome_do_ambiente pelo nome que você deseja dar ao seu ambiente virtual.

- Após executar o comando, o ambiente virtual será criado no diretório atual. Você verá uma pasta com o nome do ambiente que você escolheu.
- Para ativar o ambiente virtual, no terminal integrado, digite no terminal :

No Windows:

```

nome_do_ambiente\Scripts\activate
```

No MacOS ou Linux:

```

source nome_do_ambiente/bin/activate
```

- Lembrando que pelo fato de criar um novo ambiente vai ser necessário instalar as bibliotecas utilizadas [link](https://github.com/unb-mds/2023-2-Squad09-Gotinha/blob/main/README.md).

# Run

```
import subprocess
import json
import os
from pdf_json import url_Json


# Executa o spider e obtém a lista de dados
comando = "scrapy runspider /Users/yanlucas/2023-2-Squad09-Gotinha/Protótipos/Extrator_2/goiania_spider.py -o versao_reduzida.json"
resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE)

# Obtém o caminho do diretório atual
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define o caminho completo para o arquivo JSON
output_file_path = os.path.join(script_dir, "versao_reduzida.json")

# Renomeia o arquivo JSON gerado pelo scrapy para o caminho desejado
os.rename("versao_reduzida.json", output_file_path)

# Verifica se a lista de dados foi carregada corretamente
print("Execução bem-sucedida! O arquivo versao_reduzida.json foi gerado no mesmo diretório do script.")

# Caminho completo para o arquivo JSON gerado pelo scrapy
json_file_path = os.path.join(script_dir, "versao_reduzida.json")

# Chama a função url_Json com os dados lidos do arquivo JSON
url_Json(json_file_path)

print("Função url_Json foi executada")


```

- Foi necessário um terceiro código para que ele rode os outros dois corretamente [goiania_spider](https://github.com/unb-mds/2023-2-Squad09-Gotinha/blob/main/Protótipos/Extrator_V2/goiania_spider.py) e [pdf_json](https://github.com/unb-mds/2023-2-Squad09-Gotinha/blob/main/Protótipos/Extrator_V2/pdf_json.py).

- esse caminho '/Users/yanlucas/2023-2-Squad09-Gotinha/Protótipos/Extrator_2/goiania_spider.py' vai ter que ser mudado para o local que ele esta alocado no seu computador.

## Resultados

- Primeiramente faz a execução do goiania_spider e gera com isso um arquivo .json que possui edição, data, link e suplemento como o seguinte:
[versao_reduzida.json](https://github.com/unb-mds/2023-2-Squad09-Gotinha/blob/main/Protótipos/Extrator_V2/versao_reduzida.json)

- Posteriormente gera um arquivo que extrair os diários oficiais do documento gerado anteriormente.
[Diários em Json](https://github.com/unb-mds/2023-2-Squad09-Gotinha/tree/main/Protótipos/Extrator_V2/Diários%20em%20json)



