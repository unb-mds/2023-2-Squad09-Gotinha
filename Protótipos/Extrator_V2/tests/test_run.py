import os
import subprocess
import pytest

# Caminho para o script run.py
script_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'run.py')

# Define constantes para os nomes dos arquivos e diretórios
edicoes_recentes_json = 'edicoes_recentes.json'
diarios_em_json = 'Diários em json'
trechos_filtrados_json = 'trechos_filtrados.json'

def run_script():
    # Executa o script run.py
    subprocess.run(['python', script_path])

def assert_file_exists(file_path, message):
    # Verifica se o arquivo ou diretório existe
    assert os.path.exists(file_path), message

def test_run_script():
    """
    Testa a execução do script run.py e verifica a existência dos arquivos/diretórios gerados.
    """
    run_script()
    assert_file_exists(edicoes_recentes_json, f"O arquivo '{edicoes_recentes_json}' não foi gerado")
    assert_file_exists(diarios_em_json, f"O diretório '{diarios_em_json}' não foi gerado")
    assert_file_exists(trechos_filtrados_json, f"O arquivo '{trechos_filtrados_json}' não foi gerado")

# Teste de Regressão
def test_regressao_run_script():
    """
    Testa a regressão do script run.py, garantindo que continua funcionando conforme esperado após alterações.
    """
    run_script()
    assert_file_exists(edicoes_recentes_json, f"O arquivo '{edicoes_recentes_json}' não foi gerado após a regressão")
    assert_file_exists(diarios_em_json, f"O diretório '{diarios_em_json}' não foi gerado após a regressão")
    assert_file_exists(trechos_filtrados_json, f"O arquivo '{trechos_filtrados_json}' não foi gerado após a regressão")

# Teste de Cobertura de Código
def test_cobertura_run_script():
    """
    Testa a cobertura de código do script run.py, verificando a existência dos arquivos/diretórios gerados.
    """
    run_script()
    assert_file_exists(edicoes_recentes_json, f"O arquivo '{edicoes_recentes_json}' não foi gerado para a cobertura")
    assert_file_exists(diarios_em_json, f"O diretório '{diarios_em_json}' não foi gerado para a cobertura")
    assert_file_exists(trechos_filtrados_json, f"O arquivo '{trechos_filtrados_json}' não foi gerado para a cobertura")

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    pytest.main()
