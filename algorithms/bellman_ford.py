__author__ = 'Vemund'


matrix = [
    [99,3,99,99,99,99,99],
    [99,99,4,9,99,5,99],
    [99,99,99,4,-10,99,99],
    [3,99,99,99,99,99,1],
    [99,99,99,5,99,99,4],
    [4,99,99,99,1,99,99],
    [99,99,99,99,99,-4,99]
]

nodes = [0,99,99,99,99,99,99]
parents = [None, None, None, None, None, None, None]

def relax(u,v,w):
    if nodes[v] > nodes[u] + w:
        nodes[v] = nodes[u] + w
        parents[v] = u

for node in range(len(nodes)):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            relax(i, j, matrix[i][j])

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if nodes[i] > nodes[j] + matrix[i][j]:
            print 'NEGATIVE CYCLE DETECTED'
            print 'THE CYCLE IS AT', i, 'AND THE PARENT IS', j
print nodes
