def main():
    from sys import stdin
    from itertools import repeat
    import operator

    def quick_sort(liste, lo, hi):
        if lo < hi:
            p = partition(liste, lo, hi)
            quick_sort(liste, lo, p - 1)
            quick_sort(liste, p + 1, hi)

    def partition(liste, lo, hi):
        pivot = liste[hi][0]
        i = lo
        for j in range(lo, hi):
            if liste[j][0] <= pivot:
                liste[i], liste[j] = liste[j], liste[i]
                i += 1
        liste[i], liste[hi] = liste[hi], liste[i]
        return i

    decks = []
    for line in stdin:
        (bokstav, liste) = line.split(':')
        decks.extend(zip(map(int, liste.split(',')), repeat(bokstav)))
    quick_sort(decks, 0, len(decks) - 1)
    print "".join(map(operator.itemgetter(1), decks))
main()
