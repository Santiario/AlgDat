from collections import deque
from sys import stdin


class Node:
    def __init__(self):
        self.b = []
        self.a = False
        self.d = -1


def dfs(r):
    ns = deque()
    r.d = 0
    ns.append(r)
    while ns:
        n = ns.pop()
        if n.a:
            return n.d
        for b in n.b:
            b.d = n.d + 1
            ns.append(b)


def bfs(r):
    nk = deque()
    r.d = 0
    nk.appendleft(r)
    while nk:
        n = nk.pop()
        if n.a:
            return n.d
        for b in n.b:
            b.d = n.d + 1
            nk.appendleft(b)

def vfs(r):
    pass


def main():
    funksjon = stdin.readline().rstrip()
    antall_noder = int(stdin.readline())
    noder = []
    for i in range(antall_noder):
        noder.append(Node())
    start_node = noder[int(stdin.readline())]
    ratatosk_node = noder[int(stdin.readline())]
    ratatosk_node.a = True
    for linje in stdin:
        tall = linje.split()
        temp_node = noder[int(tall.pop(0))]
        for barn_nr in tall:
            temp_node.b.append(noder[int(barn_nr)])

    if funksjon == 'dfs':
        print dfs(start_node)
    elif funksjon == 'bfs':
        print bfs(start_node)
    elif funksjon == 'velg':
        print bfs(start_node)
main()