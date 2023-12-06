import sys
import pytest
import coverage
import tempfile
import os

# Configurando e iniciando a cobertura de código
cov = coverage.Coverage(source=['filtro'], omit=['*test*'])
cov.start()

# Adicionando o diretório principal ao sys.path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))

# Importando o módulo 'extrair_trechos' após configurar sys.path
from filtro import extrair_trechos

# Teste de Unidade Básico: Verifica se a função extrair_trechos produz os resultados esperados
def test_extrair_trechos():
    # Criando um arquivo temporário com conteúdo específico para verificar o filtro
    conteudo_teste = """
    Aqui está um exemplo de DECRETO ORÇAMENTÁRIO.
    Detalhes importantes sobre o orçamento.
    R$ 100.00 no valor total.
    """
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as arquivo_teste:
        arquivo_teste.write(conteudo_teste)
        arquivo_teste_path = arquivo_teste.name

    # Chamando a função de extração
    trechos = extrair_trechos(arquivo_teste_path)

    # Verificando se o trecho foi extraído corretamente
    assert len(trechos) == 1
    assert "DECRETO ORÇAMENTÁRIO" in trechos[0]['Trecho']
    assert "R$ 100.00" in trechos[0]['Trecho']

# Teste de Regressão: Garante que todas as funcionalidades existentes são mantidas após alterações recentes
def test_regressao_funcionalidades_existente():
    test_extrair_trechos()

# Finalizando a cobertura e gerando o relatório
cov.stop()
cov.save()
cov.report()
cov.html_report(directory='covhtml')

# Executando os testes automaticamente usando pytest
pytest.main()
