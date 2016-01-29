__author__ = 'vemund'

liste = [1, 2, 3]


def perm(liste):
    if len(liste) == 1:
        return liste
    else:
        permutations = []
        for i in range(len(liste)):
            for subliste in perm(liste[:i] + liste[i + 1:]):
                permutations.append([list(liste[i]) + subliste])
        return permutations

print "-----------"
for permutasjon in perm(liste):
    print permutasjon