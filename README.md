# Laboratório 11 de Python: Batalha Naval

11° projeto para submissão em Python de MC102 (Algoritmos e Programação de Computadores), curso ministrado pela UNICAMP.

Dando continuidade aos projetos desenvolvidos nos laboratórios de MC102 (explicação no repositório [IniciandoEmPython](https://github.com/laratoledom/IniciandoEmPython/blob/main/README.md)), temos como proposta de desenvolvimento do código o seguinte problema:
________________________________________________________________________________________________________________________________________________________________

"O objetivo desse laboratório é simular um jogo de batalha naval. O jogo possui dois jogadores, cada um com um tabuleiro quadrado 10x10 e com navios representados por peças 1 x n (com diferentes valores de n).

Na primeira parte do jogo, os jogadores devem distribuir os navios no tabuleiro, sendo que cada navio pode ser posicionado na vertical ou na horizontal e dois navios não podem ocupar uma mesma casa do tabuleiro. Na segunda parte, cada jogador tenta adivinhar as posições dos navios de seu oponente dando palpites sobre quais posições estão ocupadas. Um palpite consiste de um par (l, c) indicando a linha e a coluna onde o navio se encontra. 

As linhas são representadas pelas letras de 'A' até 'J' ('A' é a primeira linha, de cima para baixo) e as colunas são representadas pelos números de 1 até 10 (1 é a coluna mais à esquerda). Sempre que um jogador acertar todas as posições ocupadas por um navio, ele afunda esse navio. O jogador que tiver todos os seus navios afundados perde o jogo.

Para a nossa simulação, vamos assumir que você recebe como entrada um tabuleiro pronto com letras indicando a posição de cada navio e uma sequência de palpites do seu adversário. Para cada palpite você deve imprimir na saída uma das seguintes respostas:

•	<b>"agua"</b>: caso esse palpite não acerte nenhum navio. <br>
•	<b>"atingiu o navio X"</b>: caso esse palpite acerte o navio representado pela letra X, mas ainda existam posições não atingidas desse navio.<br>
•	<b>"afundou o navio X"</b>: caso esse palpite acerte o navio representado pela letra X e não existam posições não atingidas desse navio.<br>

Você pode assumir que cada navio é representado por uma letra diferente e cada navio tem tamanho 1 x n, sendo que 1 ≤ n ≤ 5.

A entrada será composta por 10 linhas representando o tabuleiro, os navios serão representados por letras e as demais casas terão o caractere '.'. A linha seguinte ao tabuleiro irá conter um número P indicando o número de palpites a serem lidos, seguida de P linhas com cada um dos palpites. Cada palpite será da forma L C onde L é uma letra de 'A' até 'J' representando a linha e C é um número de 1 até 10 representando a coluna. Você pode supor que não existem dois palpites com a mesma posição.

A saída deverá conter P linhas cada uma com a resposta para o palpite correspondente."
________________________________________________________________________________________________________________________________________________________________

<b>Observações:</b>
O arquivo foi executado através do PyCharm e no arquivo "testes" podem ser encontrados alguns exemplos de testes que verificam o código.

