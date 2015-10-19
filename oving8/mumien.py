__author__ = 'Vemund'


def main():

    from sys import stdin

    n = int(stdin.readline())
    sannsynligheter = map(float, stdin.readline().split())
    nabomatrise = []
    for linje in stdin:
        naborad = [0] * n
        naboer = map(int, linje.split())
        for nabo in naboer:
            naborad[nabo] = 1
        nabomatrise.append(naborad)

    parents = [None]*len(sannsynligheter)
    weights = [0]*len(sannsynligheter)
    weights[0] = sannsynligheter[0]
    noder = [x for x in range(len(sannsynligheter))]
    visited = set()
    while len(noder) > 0:
        highest = weights[noder[0]]
        node = noder[0]
        for i in noder:
            if weights[i] > highest:
                highest = weights[i]
                node = i
        noder.pop(noder.index(node))
        if node in visited:
            continue
        visited.add(node)
        for i in range(len(nabomatrise)):
            if nabomatrise[node][i] == 1 and weights[i] < weights[node]*sannsynligheter[i]:
                weights[i] = weights[node]*sannsynligheter[i]
                parents[i] = node
        if node == len(nabomatrise) - 1:
            break
    path = [str(len(parents) - 1)]
    parent = parents[-1]
    changed = False
    while parent is not None:
        path.append(str(parent))
        parent = parents[parent]
        changed = True
    if changed:
        print "-".join(path[::-1])
    else:
        print '0'

main()
