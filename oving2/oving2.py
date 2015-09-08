from Queue import Queue
from sys import stdin

__author__ = 'Vemund'


class Node:
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.distance = -1


def dfs(rot):
    node_stakk = []
    rot.distance = 0
    node_stakk.append(rot)
    while not len(node_stakk)== 0:
        node = node_stakk.pop()
        if node.ratatosk:
            return node.distance
        for barn in node.barn:
            if barn.distance == -1:
                barn.distance = node.distance +1
                node_stakk.append(barn)


def bfs(rot):
    node_ko = Queue()
    rot.distance = 0
    node_ko.put_nowait(rot)
    while not node_ko.empty():
        node = node_ko.get_nowait()
        if node.ratatosk:
            return node.distance
        for child in node.barn:
            if child.distance == -1:
                child.distance = node.distance +1
                node_ko.put_nowait(child)


def main():
    funksjon = stdin.readline().strip()
    antall_noder = int(stdin.readline())
    noder = []
    for i in range(antall_noder):
        noder.append(Node())
    start_node = noder[int(stdin.readline())]
    ratatosk_node = noder[int(stdin.readline())]
    ratatosk_node.ratatosk = True
    for linje in stdin:
        tall = linje.split()
        temp_node = noder[int(tall.pop(0))]
        for barn_nr in tall:
            temp_node.barn.append(noder[int(barn_nr)])

    if funksjon == 'dfs':
        print dfs(start_node)
    elif funksjon == 'bfs':
        print bfs(start_node)
    elif funksjon == 'velg':
        print dfs(start_node)
main()