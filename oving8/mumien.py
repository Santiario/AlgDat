__author__ = 'Vemund'


def main():

    from sys import stdin

    n = int(stdin.readline())
    sannsynligheter = map(float, stdin.readline().split())
    nabomatrise = [[] for x in range(n)]
    for i in range(n):
        naborad = [0] * n
        naboer = map(int, stdin.readline().split())
        for nabo in naboer:
            naborad[nabo] = 1
        nabomatrise[i] = naborad

    parents = [None]*n
    weights = [0]*n
    weights[0] = sannsynligheter[0]
    noder = [x for x in range(n)]
    while len(noder) > 0:
        highest = weights[noder[0]]
        node = noder[0]
        for i in noder:
            if weights[i] > highest:
                highest = weights[i]
                node = i
        noder.pop(noder.index(node))
        for i in range(n):
            if nabomatrise[node][i] == 1 and weights[i] < weights[node]*sannsynligheter[i]:
                weights[i] = weights[node]*sannsynligheter[i]
                parents[i] = node
        if node == n - 1:
            break
    if parents[-1] is None:
        print 0
    else:
        path = [str(n - 1)]
        parent = parents[-1]
        while parent is not None:
            path.append(str(parent))
            parent = parents[parent]
        print "-".join(path[::-1])

main()
