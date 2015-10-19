__author__ = 'Vemund'

def main():
    from sys import stdin

    def remove_highest(noder, weights):
        highest = weights[noder[0]]
        index = noder[0]
        for i in noder:
            if weights[i] > highest:
                highest = weights[i]
                index = i
        noder.pop(noder.index(index))
        return index

    def relax(edge_from, edge_to, weights, parents, sannsynligheter):
        if weights[edge_to] < weights[edge_from]*sannsynligheter[edge_to]:
            weights[edge_to] = weights[edge_from]*sannsynligheter[edge_to]
            parents[edge_to] = edge_from
            #print 'Setter node', edge_to, 'til aa ha parent', edge_from

    def beste_sti(nabomatrise, sannsynligheter):
        parents = [None]*len(sannsynligheter)
        weights = [0]*len(sannsynligheter)
        weights[0] = sannsynligheter[0]
        noder = [x for x in range(len(sannsynligheter))]
        visited = set()
        while len(noder) > 0:
            node = remove_highest(noder, weights)
            if node in visited:
                continue
            visited.add(node)
            #print 'Tar for oss node nr', node, 'som har (beste) verdi', weights[node]
            #print sorted(visited)
            for i in range(len(nabomatrise)):
                if nabomatrise[node][i] == 1:
                    relax(node, i, weights, parents, sannsynligheter)
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
            return "-".join(path[::-1])
        else:
            return '0'




    n = int(stdin.readline())
    sannsynligheter = map(float, stdin.readline().split())
    nabomatrise = []
    for linje in stdin:
        naborad = [0] * n
        naboer = map(int, linje.split())
        for nabo in naboer:
            naborad[nabo] = 1
        nabomatrise.append(naborad)
    #for rad in nabomatrise:
        #print rad
    print beste_sti(nabomatrise, sannsynligheter)

main()
