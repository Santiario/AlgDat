def quick_sort(liste, lo, hi):
    if lo < hi:
        p = partition(liste, lo, hi)
        quick_sort(liste, lo, p - 1)
        quick_sort(liste, p + 1, hi)

def partition(liste, lo, hi):
    pivot = liste[hi]
    i = lo
    for j in range(lo, hi):
        if liste[j] <= pivot:
            liste[i], liste[j] = liste[j], liste[i]
            i += 1
    liste[i], liste[hi] = liste[hi], liste[i]
    return i

def binary_search(liste, value):
    low = 0
    high = len(liste)-1
    while low <= high:
        mid = (low+high)//2
        if liste[mid] > value:
            high = mid-1
        elif liste[mid] < value:
            low = mid+1
        else:
            return mid
    return -1

def finn(liste, nedre, ovre):
    pass

    # Merk: resultatet ma returneres
    # SKRIV DIN KODE HER

def main():
    from sys import stdin
    liste = []
    for x in stdin.readline().split():
        liste.append(int(x)) #  Kanskje mulig å gjøre dette raskere?

    quick_sort(liste, 0, len(liste) - 1)

    for linje in stdin:
        ord = linje.split()
        minst = int(ord[0])
        maks = int(ord[1])
        resultat = finn(list, minst, maks)
        print str(resultat[0]) + " " + str(resultat[1])

main()