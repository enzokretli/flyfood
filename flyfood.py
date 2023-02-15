import time

inicio=time.process_time()

def permutacao(lista):
    if len(lista) <= 1:
        return [lista]
    lista_auxiliar = []
    for indice, elemento in enumerate(lista):
        restantes = lista[:indice] + lista[indice+1:]
        for p in permutacao(restantes):
            lista_auxiliar.append([elemento]+p)
    return lista_auxiliar

def calcular_custo(lista):
    caminho = []
    for i in range(len(lista)-1):
        distancia_total = 0
        diferença1 = abs(coordenadas[lista[i]][0] - coordenadas[lista[i+1]][0])
        diferença2 = abs(coordenadas[lista[i]][1] - coordenadas[lista[i+1]][1])
        distancia_total += diferença1 + diferença2
        caminho.append(distancia_total)
    return sum(caminho)

arquivo = open("matriz7.txt", 'r')
pontos_de_entrega = []
coordenadas = {}
custos = []
num_linhas, num_colunas = [int(x) for x in arquivo.readline().split()]
for linhas in range(num_linhas):
    linha = arquivo.readline().split()
    for colunas in range(num_colunas):
        if linha[colunas] != '0':
            if linha[colunas] != 'R': 
                pontos_de_entrega.append(linha[colunas])            
        if linha[colunas] in pontos_de_entrega or linha[colunas] == 'R':
            coordenadas[linha[colunas]] = (linhas, colunas)
permutacao_pontos = permutacao(pontos_de_entrega)

for caminhos in permutacao_pontos:
    caminhos.insert(0, 'R')
    caminhos.append('R')
    custo = calcular_custo(caminhos)
    custos.append(custo)
indice_caminho = custos.index(min(custos))
menor_caminho = ''.join(str(caminhos) for caminhos in permutacao_pontos[indice_caminho] if caminhos != 'R')
print(menor_caminho)

fim=time.process_time()
tempo=fim-inicio
print(f'{tempo:.5f}')
