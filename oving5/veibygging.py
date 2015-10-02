from sys import stdin
__author__ = 'vemund'

Inf = float(1e3000)


def mst(nm):
    nodeliste = set()
    nodeliste.add(0)
    heaviest = -Inf
    while True:
        shortest = Inf
        neste_kant = Inf
        for vertice in nodeliste:
            for edge, weight in enumerate(nm[vertice]):
                if weight < shortest:
                    if vertice not in nodeliste and edge in nodeliste:
                            neste_kant = vertice
                            shortest = weight
                    elif vertice in nodeliste and edge not in nodeliste:
                            neste_kant = edge
                            shortest = weight
        if shortest == Inf:
            break
        else:
            nodeliste.add(neste_kant)
            if shortest > heaviest:
                heaviest = shortest
    return heaviest


def main():
    linjer = []
    for string in stdin:
        linjer.append(string)
    n = len(linjer)
    nabomatrise = [None] * n
    node = 0
    for linje in linjer:
        nabomatrise[node] = [Inf] * n
        for k in linje.split():
            data = k.split(':')
            nabo = int(data[0])
            vekt = int(data[1])
            nabomatrise[node][nabo] = vekt
        node += 1
    print mst(nabomatrise)
