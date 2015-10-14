__author__ = 'Vemund'


class Heap:
    def __init__(self):
        self.array = list()
        self.heap_size = 0

    def __getitem__(self, item):
        return self.array[item]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __len__(self):
        return len(self.array)


def parent(i):
    return i//2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def max_heapify(H, i):
    l = left(i)
    r = right(i)
    if l <= H.heap_size and H[l] > H[i]:
        largest = l
    else:
        largest = i
    if r <= H.heap_size and H[r] > H[largest]:
        largest = r
    if largest != i:
        H[i], H[largest] = H[largest], H[i]
        max_heapify(H, largest)

def min_heapify(H, i):
    l = left(i)
    r = right(i)
    if l <= H.heap_size and H[l] < H[i]:
        smallest = l
    else:
        smallest = i
    if r <= H.heap_size and H[r] < H[smallest]:
        smallest = r
    if smallest != i:
        H[i], H[smallest] = H[smallest], H[i]
        max_heapify(H, smallest)


def build_max_heap(H):
    H.heap_size = H.length
    for i in range(H.length//2, 0, -1):
        max_heapify(H, i)


def build_min_heap(H):
    H.heap_size = H.length
    for i in range(H.length//2, 0, -1):
        min_heapify(H, i)


def min_heapsort(H):
    build_min_heap(H)
    for i in range(len(H) - 1, 0, -1):
        H[1], H[i] = H[i], H[1]
        H.heap_size -= 1
        min_heapify(H, 1)

def max_heapsort(H):
    build_max_heap(H)
    for i in range(len(H) - 1, 0, -1):
        H[1], H[i] = H[i], H[1]
        H.heap_size -= 1
        max_heapify(H, 1)

def heap_max(H):
    return H[1]

def heap_min(H):
    return H[1]

def heap_extract_max(H):
    if H.heap_size < 1:
        raise ValueError('Trying to extract maximum element from an empty heap')
    maximum = H[1]
    H[1] = H[H.heap_size]
    H.heap_size -= 1
    max_heapify(H, 1)
    return maximum


def heap_extract_min(H):
    if H.heap_size < 1:
        raise ValueError('Trying to extract maximum element from an empty heap')
    minimum = H[1]
    H[1] = H[H.heap_size]
    H.heap_size -= 1
    min_heapify(H, 1)
    return minimum


