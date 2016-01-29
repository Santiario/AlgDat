
__author__ = 'vemund'

def summer(A, B):
    stop = max(B)
    koe = [0]
    while koe:
        i = koe.pop()
        j = i
        sum = 0
        while j < len(A):
            sum += A[j]
            for k in range(len(B)):
                if sum == B[k]:
                    koe.insert(0, j + 1)
                    if j + 1 == len(A):
                        return True
            j += 1
    return False
#             0 1 2 3 4 5 6  7
print summer([2,4,5,1,2,2,9,-5], [6, 8])