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


def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result



print list1
list1 = merge_sort(list1)
print list1