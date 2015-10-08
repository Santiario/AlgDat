__author__ = 'Vemund'

liste = [0.234,0.345,0.342,0.264,0.4224,0.3632,0.6252,0.3453,0.5555,0.999]

def bucket_sort(list):
    print(list)
    n = len(list)
    bucket = []
    for i in range(n):
        bucket.append([])
    for i in range(n):
        bucket[int(n*list[i])].append(list[i])
    for i in range(n):
        bucket[i].sort()
    result_list = []
    for i in range(n):
        result_list.extend(bucket[i])
    return result_list


def insertion_sort(list):
    print list
    result_list = [list[0]]
    for i in range(1,len(list)):
        for j in range(0,len(result_list)):
            if list[i] <= result_list[j]:
                result_list.insert(j, list[i])
                break
            elif j == len(result_list)-1:
                result_list.append(list[i])
    return result_list


list1 = [1,2,3,4,78,9,6,2,3,5,6,8,9,4,2,6,0,3,1,56,253,62,5]
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

print list1
quick_sort(list1, 0, len(list1) - 1)
print list1