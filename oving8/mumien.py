__author__ = 'Vemund'

def main():
    from sys import stdin

    def beste_sti(nm, sans):
        pass

    n = int(stdin.readline())
    sannsynligheter = map(float, stdin.readline().split())
    nabomatrise = []
    for linje in stdin:
        naborad = [0] * n
        naboer = [int(nabo) for nabo in linje.split()]
        for nabo in naboer:
            naborad[nabo] = 1
        nabomatrise.append(naborad)
    print beste_sti(nabomatrise, sannsynligheter)

main()