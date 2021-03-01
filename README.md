# Benchmark-AD CLI

O Benchmark-AD CLI é uma implementação de benchmark para análise de desempenho de sistemas computacionais com ambiente Linux. 

Desenvolvido para ambientes Linux, utilizando as linguagens: Python e Shell Script.
Executa uma série de operações de Álgebra Linear com inteiro e ponto flutuante a fim de analisar o desempenho da CPU da máquina. 
Além disso, realiza testes de escrita e leitura no Disco Rígido e na memória principal. 
Ao final, exibe gráficos e relatórios de desempenho com auxílio das bibliotecas Pandas, Numpy e Matplotlib.

Informações sobre seu funcionamento:
  - O módulo principal, benchmark-ad.sh, de interação com o usuário é desenvolvido em Shell Script, possibilitando seu uso no terminal;
  - O usuário deve passar dois parâmetros: Número de Testes e Nível da Carga de Trabalho;
  - Após validar os parâmetros fornecidos pelo usuário, o módulo principal faz chamadas aos módulos de teste: benchmark-cpu.py, benchmark-mem.sh e benchmark-hd.sh.
  - Os dados obtidos são armazenados em arquivos .csv e lidos pelo módulo de geração de relatório e gráficos, resultado.py, que utiliza as bibliotecas numpy, pandas e matplotlib para tratamento e geração de gráficos e dados estatísticos.

As métricas analisadas são: 
  - CPU: Tempo de execução de operações de álgebra linear com matrizes (em segundos).
  - Disco Rígido: Taxa de Leitura e Escrita de dados (em MB/s)
  - Memória Principal: Taxa de Leitura e Escrita de dados (em GB/s)

As cargas de trabalho são divididas em 3 níveis como a seguir: 
  Baixo:
    - Utiliza operações em matrizes 512x512 para teste de CPU;
    - Utiliza 400 MB de dados para teste de HD;
    - Utiliza 512 MB de dados para teste de Memória Principal.
  Moderado:
    - Utiliza operações em matrizes 1024x1024 para teste de CPU;
    - Utiliza 800 MB de dados para teste de HD;
    - Utiliza 1 GB de dados para teste de Memória Principal.
  Alto:
    - Utiliza operações em matrizes 2048x2048 para teste de CPU;
    - Utiliza 1.6 GB de dados para teste de HD;
    - Utiliza 2 GB de dados para teste de Memória Principal.


PROCESSO DE INSTALAÇÃO

A instalação é muito simples, basta baixar os arquivos na estrutura que aparecem aqui e tornar os scripts executáveis. Após isso, execute o script "benchmark-ad.sh [repeticoes] [nivel]" na pasta principal. O parâmentro [repeticoes] é um número inteiro que define a quantidade de repetições para os testes de desempenho. Já o parâmetro [nivel] é um número inteiro entre 1 e 3, que define o nível da carga de trabalho a ser aplicada aos testes (1 - Baixo, 2 - Moderado, 3 - Alto).
  
Ao executar o script principal, automaticamente será feita a verificação das dependências necessárias, em caso de não encontrar os pacotes necessários o programa faz o download e instalação das dependências. São elas:

  - Gerenciador de Pacotes do Python: pip;
  - Bibliotecas do Python: numpy, pandas e matplotlib.

* O único requisito é ter o Python 3 instalado na máquina



O código pode ser modificado e utilizado livremente.
Para as próximas versões, espera-se:
  - Implementar os módulos de benchmark seguindo as especificações da SPEC, utilizando métricas de velocidade e taxa, aplicando médias harmônicas e geométricas para determinação do score obtido em cada teste;
  - Implementar um módulo de comparação, responsável por comparar o desempenho da máquina de teste com uma máquina referência.

Compartilhe e contribua com esse projeto!

Créditos: Prof. Lucas Ferreira Mendes
