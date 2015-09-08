from collections import deque
from sys import stdin


class Node:
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.distance = -1


def dfs(rot):
    node_stakk = deque()
    rot.distance = 0
    node_stakk.append(rot)
    while node_stakk:
        node = node_stakk.pop()
        if node.ratatosk:
            return node.distance
        for barn in node.barn:
            if barn.distance == -1:
                barn.distance = node.distance + 1
                node_stakk.append(barn)


def bfs(rot):
    node_ko = deque()
    rot.distance = 0
    node_ko.appendleft(rot)
    while node_ko:
        node = node_ko.pop()
        if node.ratatosk:
            return node.distance
        for child in node.barn:
            if child.distance == -1:
                child.distance = node.distance + 1
                node_ko.appendleft(child)


def main():
    funksjon = stdin.readline().rstrip()
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
        print bfs(start_node)
main()