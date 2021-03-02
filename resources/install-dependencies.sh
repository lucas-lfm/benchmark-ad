#!/bin/bash

#################################################################################
#                                                                               #
# Nome: install-dependencies.sh                                                 #
#                                                                               #
# Autor: Lucas Mendes (lucas.mendes@ifce.edu.br)                                #
# Data: 26/02/2021                                                              #
#                                                                               #
# Descrição: Verifica e instala as dependências necessárias para a execução do  #
#		programa de benchmark.  					#																					#
#                                                                               #
# Uso: ./install-dependencies.sh                                                #
#                                                                               #
#################################################################################

# Verifica existência da pasta resultados, utilizada para armazenar os arquivos .csv
if [[ ! -d "resources/resultados" ]]; then
	mkdir resources/resultados
	chmod 775 resources/resultados
fi

# Verifica se o gerenciador de pacotes pip3 está instalado, caso contrário realiza a instalação
if [[ ! $(which pip3) ]]; then
	echo "Baixando pip..."
	echo
	sudo wget https://bootstrap.pypa.io/get-pip.py
	echo "Download finalizado!"
	echo
	echo "Instalando pip..."
	echo
	sudo python3 get-pip.py
	
	# Verifica se o comando anterior, que tenta fazer a instalação através do arquivo baixado, foi bem sucedido
	# Caso contrário realiza a instalação pelo apt
	if [[ $? -ne 0 ]]; then
		sudo apt -y install python3-pip
	fi
	
	rm -f get-pip.py
	echo "Instalação concluída!"
	echo
fi

if [[ $(which pip3) ]]; then
	if [[ ! $(pip3 list | grep numpy) ]]; then
		echo "Instalando módulo numpy..."
		echo
		sudo pip3 install numpy
		echo "Instalação de módulo concluída!"
		echo
	fi
	if [[ ! $(pip3 list | grep matplotlib) ]]; then
		echo "Instalando módulo matplotlib..."
		echo
		sudo pip3 install matplotlib
		echo "Instalação de módulo concluída!"
		echo
	fi
	if [[ ! $(pip3 list | grep pandas) ]]; then
		echo "Instalando módulo pandas..."
		echo
		sudo pip3 install pandas
		echo "Instalação de módulo concluída!"
		echo
	fi
fi

exit 0
