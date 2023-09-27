"""
    Antes de utilizar o programa, certifique-se que você tem as bibliotecas instaladas em sua máquina 
    Para instalar as bibliotecas, abra o terminal ou prompt de comando e digite:
    pip install selenium
    pip install webdriver-manager
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from msvcrt import getwch

# Função para esconder a senha com asterístico, já que o terminal do vscode não suporta o getpass
def mask_input(prompt='', mask='*'):
    print(prompt, end='', flush=True)
    response = ''
    while (char := getwch()) != '\r':
        if char == '\x08':
            print('\b \b', end='', flush=True)
            response = response[:-1]
        else:
            response += char
            print(mask, end='', flush=True)
    print("")
    return response

while True:
    matricula = input('Digite sua matrícula: ')
    senha = mask_input('Digite sua senha: ')

    # Instala o chromedriver manager automaticamente
    service = Service(ChromeDriverManager().install())

    chrome = webdriver.Chrome(service=service)  # Inicia o chrome

    # Abre o site desejado
    chrome.get(
        'https://autenticacao.unb.br/sso-server/login?service=https%3A%2F%2Fsig.unb.br%2Fsigaa%2Flogin%2Fcas')

    try:
        entrada_matricula = chrome.find_element('xpath', '//*[@id="username"]')
        entrada_matricula.clear()
        entrada_matricula.send_keys(matricula)
        entrada_senha = chrome.find_element('xpath', '//*[@id="password"]')
        entrada_senha.clear()
        entrada_senha.send_keys(senha)
        login = chrome.find_element('xpath', '//*[@id="login-form"]/button')
        login.click()
        cookie = chrome.find_element('xpath', '//*[@id="sigaa-cookie-consent"]/button')
        cookie.click()
        chrome.find_element('xpath', '//*[@id="menu_form_menu_discente_j_id_jsp_340461267_98_menu"]/table/tbody/tr/td[1]').click()
        chrome.find_element('xpath', '//*[@id="cmSubMenuID1"]/table/tbody/tr[1]').click()
        tabela = chrome.find_element('xpath', '//*[@id="relatorio"]/div')
        """titulo = 1
        for i in range(1 , numero_de_tabelas + 1):
            print(f"Tabela {titulo}: ")
            titulo += 1
            path_atual = f'//*[@id="relatorio"]/div/table[{i}]'
            tabela = chrome.find_element_by_xpath(path_atual)
            print(f"Conteúdo da tabela {i}:")
            print(tabela.text)
            print("\n")"""
        print(tabela.text)
        chrome.quit()
        break  # Interrompe o loop se o login for bem-sucedido
    except:
        print('Erro ao logar no SIGAA')
        print('Verifique se a matrícula e senha estão corretas')
        chrome.quit()
        time.sleep(1)  # Espera 1 segundo antes de tentar novamente