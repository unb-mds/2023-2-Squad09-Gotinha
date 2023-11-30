#!/bin/bash

# Criação do ambiente virtual
python3 -m venv GOTA

# Ativação do ambiente virtual
source GOTA/bin/activate

# Instalação de dependências a partir do arquivo requirements.txt
pip install -r requirements.txt

# Mensagem indicando que o ambiente virtual foi configurado
echo "Ambiente virtual configurado. Execute 'source venv/bin/activate' para ativá-lo."