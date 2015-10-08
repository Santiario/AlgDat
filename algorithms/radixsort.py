__author__ = 'Vemund'

liste = [1,4,6,7,1,2,6,9,3,2,6,0,0,345,12,313,8,3,4123,1231,123,1231,231,6,67,5]

def radixsort(liste):
  lengde = False
  plass = 1

  while not lengde:
    lengde = True
    buckets = [[] for i in range(10)]

    for i in liste:
      temp = i / plass
      buckets[temp % 10].append(i)
      if lengde and temp > 0:
        lengde = False

    n = 0
    for i in range(10):
      buck = buckets[i]
      for j in buck:
        liste[n] = j
        n += 1

    plass *= 10

print liste
radixsort(liste)
print liste