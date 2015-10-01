from sys import stdin


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    toppnode = Node()
    for tuppel in ordliste:
        node = toppnode
        word = tuppel[0]
        i = 0
        while i < len(word):
            if word[i] in node.barn.keys():
                node = node.barn[word[i]]
            else:
                node.barn[word[i]] = Node()
                node = node.barn[word[i]]
            i += 1
            if i == len(word):
                node.posi.append(tuppel[1])
    return toppnode


def posisjoner(ord, indeks, node):
    if indeks == len(ord):
        return node.posi
    elif ord[indeks] == '?':
        result = []
        for key in node.barn.keys():
            result.extend(posisjoner(ord, indeks + 1, node.barn[key]))
        return result
    elif ord[indeks] in node.barn.keys():
        return posisjoner(ord, indeks + 1, node.barn[ord[indeks]])
    else:
        return []


def main():
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append((o, pos))
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print sokeord + ":",
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print p,
        print
main()
