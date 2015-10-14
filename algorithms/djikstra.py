__author__ = 'Vemund'

INF = 100000000

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.distance = 10000000

nodes = [Node(0), Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)]

matrix4a = [
    [99,3,99,99,99,99,99],
    [99,99,40,9,99,5,99],
    [99,99,99,40,5,99,99],
    [3,99,99,99,99,99,1],
    [99,99,99,5,99,99,4],
    [4,99,99,99,10,99,99],
    [99,99,99,99,99,2,99]
]

matrix4c = [
    [99,3,99,99,99,99,99],
    [99,99,2,5,99,99,5],
    [99,99,99,4,2,99,99],
    [4,99,99,99,99,1,99],
    [99,99,99,99,99,6,99],
    [99,99,99,99,99,99,3],
    [4,99,99,99,8,99,99]
]

def extract_min(q):
    minimum_index = 0
    for i in range(len(q)):
        if q[i].distance < q[minimum_index].distance:
            minimum_index = i
    return q.pop(minimum_index)


def initialize():
    for node in nodes:
        node.distance = 10000000
    nodes[0].distance = 0

def relax(u,v,w):
    if v.distance > u.distance + w:
        v.distance = u.distance + w
        v.parent = u

def max_relax(u,v,w):
    if v.distance > max(u.distance ,w):
        v.distance = max(u.distance, w)
        v.parent = u

def dijkstra():
    initialize()
    visited = set()
    q = list(nodes)
    while q:
        u = extract_min(q).name
        #if u in visited: continue
        visited.add(u)
        for navn, node in enumerate(nodes):
            print navn,':',node.distance
        print '-----------------------'
        for v, edge in enumerate(matrix4c[u]):
            max_relax(nodes[u], nodes[v], edge)

dijkstra()

for navn, node in enumerate(nodes):
    print navn,':',node.distance

