#!/bin/bash

#################################################################################
#                                                                               #
# Nome: install-dependencies.sh                                                 #
#                                                                               #
# Autor: Lucas Mendes (lucas.mendes@ifce.edu.br)                                #
# Data: 26/02/2021                                                              #
#                                                                               #
# Descrição: Verifica e instala as dependências necessárias para a execução do  #
#		programa de benchmark.  					#
#                                                                               #
# Uso: ./install-dependencies.sh                                                #
#                                                                               #
#################################################################################

if [[ ! $(which pip) ]]; then
	echo "Baixando pip..."
	echo
	wget https://bootstrap.pypa.io/get-pip.py
	echo "Download finalizado!"
	echo
	echo "Instalando pip..."
	echo
	python3 get-pip.py
	rm get-pip.py
	echo "Instalação concluída!"
	echo
fi

if [[ $(which pip) ]]; then
	if [[ ! $(pip list | grep numpy) ]]; then
		echo "Instalando módulo numpy..."
		echo
		pip install numpy
		echo "Instalação de módulo concluída!"
		echo
	fi
fi

exit 0
