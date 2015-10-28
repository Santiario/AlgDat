__author__ = 'Vemund'
def main():
    from sys import stdin

    # kapasiteter er den opprinnelige kapasitetsmatrisen, som inneholder n x n elementer (hvor n er antall noder).
    # startrom er en liste med indeksene til nodene som tilsvarer startrommene.
    # utganger er en liste med indeksene til nodene som tilsvarer utgangene.

    def antallIsolerteStier(kapasiteter, startrom, utganger):
        for i in range(len(kapasiteter)):
            kapasiteter[i].insert(0, 0)
        for i in range(len(kapasiteter)):
            if i in utganger:
                kapasiteter[i].append(1)
            else:
                kapasiteter[i].append(0)
            kapasiteter[i].append(0)


        ny_kapa = []
        i = 1
        while i < len(kapasiteter):
            node = [0] * (len(kapasiteter) * 2)
            node[i * 2] = 1
            ny_nabo = []
            for j in range(1, len(kapasiteter[i]) - 2):
                if kapasiteter[i][j] == 1:
                    ny_nabo.extend([1, 0])
                else:
                    ny_nabo.extend([0, 0])
            ny_kapa.append(node)
            ny_kapa.append(ny_nabo)
            i += 1

        ny_superstart = [0] * (len(ny_kapa) + 2)
        for start in startrom:
            ny_superstart[start * 2 + 1] = 1
        ny_kapa.insert(0, ny_superstart)
        ny_kapa.append([0] * len(ny_superstart))



        #""" Nice print"""
        #print 'Printer kapasiteter'
        #print "  ",0,"",1,"",2,"",3,"",4,"",5,"",6,"",7,"",8
        #for i in range(len(ny_kapa)):
        #    print i, ny_kapa[i]

        flyt = [[]]*len(ny_kapa)
        for i in range(len(ny_kapa)):
            flyt[i] = [0] * len(ny_kapa)
        aug_path = finnFlytsti(0, len(ny_kapa) - 2, flyt, ny_kapa)
        #print aug_path
        while aug_path:
            for i in range(len(aug_path) - 1):
                flyt[aug_path[i]][aug_path[i + 1]] += 1
            aug_path = finnFlytsti(0, len(ny_kapa) - 2, flyt, ny_kapa)
        #print 'Ferdig!'


        #""" Nice print"""
        #print "  ",0,"",1,"",2,"",3,"",4,"",5,"",6,"",7
        #for i in range(len(flyt)):
        #    print i, flyt[i]
        return sum(flyt[0])

        # Sok gjennom grafen helt til den returnerer None


        # Du kan bruke metoden finnFlytsti for aa forenkle oppgaven.
        # SKRIV DIN KODE HER


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
        koe = [kilde]
        while koe:
            node = koe.pop(0)
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
            for nabo in range(n):
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
    #for i in range(len(nabomatrise)):
    #    print nabomatrise[i]
    print antallIsolerteStier(nabomatrise, startrom, utganger)
main()
