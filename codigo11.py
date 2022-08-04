matriz = []
for a in range(10):
    matriz.append(input().split())
linha = []
coluna = []
num_jog = int(input())
for b in range(num_jog):
    l, c = input().split()
    linha.append(l)
    coluna.append(c)
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = 0
while c < len(linha):
    pos = letras.index(linha[c])
    num = numeros[pos]
    linha[c] = num
    c = c + 1
g = 0
while g < len(linha):
    l = int(linha[g])
    c = int(coluna[g]) - 1
    if matriz[l][c] == ".":
        print("agua")
    else:
        matriz[l][c] = matriz[l][c].lower()
        maiusc = []
        u = 0
        while u < 10:
            for d in matriz[u]:
                if d == matriz[l][c].upper():
                    maiusc.append("1")
            u = u + 1
        if len(maiusc) > 0:
            print("atingiu o navio", matriz[l][c].upper())
        else:
            print("afundou o navio", matriz[l][c].upper())
    g = g + 1
