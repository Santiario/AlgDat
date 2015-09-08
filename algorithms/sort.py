__author__ = 'Vemund'

list = [0.234,0.345,0.342,0.264,0.4224,0.3632,0.6252,0.3453,0.5555,0.999]

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


print bucket_sort(list)
print
print insertion_sort(list)
