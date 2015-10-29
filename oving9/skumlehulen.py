__author__ = 'Vemund'
def main():
    from sys import stdin
    from collections import deque

    # kapasiteter er den opprinnelige kapasitetsmatrisen, som inneholder n x n elementer (hvor n er antall noder).
    # startrom er en liste med indeksene til nodene som tilsvarer startrommene.
    # utganger er en liste med indeksene til nodene som tilsvarer utgangene.

    def antallIsolerteStier(kapasiteter, startrom, utganger):
        original_n = len(kapasiteter)
        n = 2 * len(kapasiteter) + 2



        ny_kapa = [[]]* n
        for i in xrange(n):
            ny_kapa[i] = [0] * n

        for kilde in startrom:
            ny_kapa[0][kilde * 2 + 1] = 1

        for i in xrange(original_n):
            for j in xrange(original_n):
                ny_kapa[2*i+2][2*j+1] = kapasiteter[i][j]
            ny_kapa[2*i+1][2*i+2] = 1


        for i in utganger:
            ny_kapa[2*i+2][n - 1] = 1

        flyt = [[]] * n
        for i in xrange(n):
            flyt[i] = [0] * n
        sluk = n - 1
        stier = 0
        antall_innganger = len(startrom)
        antall_utganger = len(utganger)
        aug_path = finnFlytsti(0, sluk, flyt, ny_kapa)

        while aug_path:
            stier += 1
            if stier == antall_innganger or stier == antall_utganger:
                break
            for i in xrange(len(aug_path) - 1):
                flyt[aug_path[i]][aug_path[i + 1]] += 1
                flyt[aug_path[i+1]][aug_path[i]] -= 1
            aug_path = finnFlytsti(0, sluk, flyt, ny_kapa)

        return stier



    # Finner en sti fra noden med indeks 'kilde' til noden med indeks 'sluk'
    # med ledig kapasitet i et flytnettverk med flyt F og kapasitet C.
    # Returnerer en liste hvor foerste element er indeksen til en av startnodene,
    # siste element er indeksen til en av utgangene, og elementene imellom er
    # indeksene til de andre nodene paa veien som ble funnet, i riktig rekkefoelge.
    # Eksempel: en sti fra startnoden 4 til node 3, node 9, node 7 og til slutt til
    # utgangen 12 vil representeres som [4, 3, 9, 7, 12].

    def finnFlytsti(kilde, sluk, F, C):
        n = len(F)
        oppdaget = [False] * n
        forelder = [None] * len(F)
        koe = deque()
        koe.append(kilde)
        while koe:
            node = koe.pop()
            if node == sluk:
                # Har funnet sluken, lager en array med passerte noder
                sti = []
                i = node
                while True:
                    sti.append(i)
                    if i == kilde:
                        break
                    i = forelder[i]
                sti.reverse()
                return sti
            for nabo in xrange(n):
                if not oppdaget[nabo] and F[node][nabo] < C[node][nabo]:
                    koe.append(nabo)
                    oppdaget[nabo] = True
                    forelder[nabo] = node
        return None

    noder = int(stdin.readline().split()[0])
    startrom = map(int, stdin.readline().split())
    utganger = map(int, stdin.readline().split())
    nabomatrise = [[]]*noder
    for i, linje in enumerate(stdin.readlines()):
        nabomatrise[i] = map(int, linje.split())
    print antallIsolerteStier(nabomatrise, startrom, utganger)
main()
