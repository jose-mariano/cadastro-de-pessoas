# Cadastro de Pessoas com Python
Como o próprio nome já diz esse é um sistema para cadastrar pessoas, feito com python3.
Esse sistema é bem simples, a ideia é um sistema para cadastrar e visualizar as pessoas cadastradas. Nesse projeto os dados ficam salvos em um banco sqlite. O sistema ainda permite que o usúario escolha qual tipo de interface deseja utilizar, por padrão o sistema funciona com interface gráfica, mas basta adicionar CLI como argumento no momento de executar o programa e ele automaticamente irá inicializar o command line.

### Requisitos
Nesse projeto não utilizo nenhuma biblioteca além das padrões do python. Apenas certifique-se que possuí a biblioteca tkinter, para conseguir executar no modo GUI. No linux a biblioteca tkinter não vem por padrão como no windows e no mac. Para instalar essa biblioteca utilize o seguinte comando:

`sudo apt-get install python3-tk`

### Executando
Como dito acima, podemos utilizar duas interfaces diferentes, o modo CLI e o modo GUI (padrão). Abaixo segue como executar de cada maneira:

Usando modo CLI:

`python3 run.py CLI`

Usando modo GUI:

`python3 run.py GUI` ou `python3 run.py`
