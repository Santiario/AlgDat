from sys import stdin
from collections import deque
# -*- coding: utf-8 -*-

__author__ = 'Vemund'



def subgraftetthet(nabomatrise, startnode, antall_kanter):
    n = len(nabomatrise)
    visited = {startnode: True}
    besokte_kanter = 0
    besokte_noder = 1
    ko = deque()
    ko.appendleft(startnode)
    while ko:
        node = ko.pop()
        #print 'besoker naa', node
        for nabo in xrange(n):
            if nabomatrise[node][nabo] == '1':

                besokte_kanter += 1
                #print 'Fant en kant!', 'Har naa funnet', besokte_kanter, 'kanter'
                if visited.get(nabo) is None:
                    besokte_noder += 1
                    visited[nabo] = True
                    ko.appendleft(nabo)
    #print 'besokte noder:', besokte_noder
    #print 'totalt antall noder:', n
    #print 'besokte kanter', besokte_kanter
    #print 'totalt antall kanter:', antall_kanter

    if n == 0 or n-besokte_noder == 0:
        return 0.0
    else:
        return float(antall_kanter - besokte_kanter) / (float(n - besokte_noder)**2)

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


    #
    # bes_kanter, bes_noder = bfs(nabomatrise, startnode, visited, 0, 0)






def bfs2(nabomatrise, startnode, visited, besokte_kanter, besokte_noder):
    index = 0
    while index < len(nabomatrise[startnode]):
        nabo = nabomatrise[startnode][index]
        if nabo == '1':
            besokte_kanter += 1
            if visited.get(index) is None:
                besokte_noder += 1
                visited[index] = True
                nye_kanter, nye_noder = bfs(nabomatrise, index, visited, besokte_kanter, besokte_noder)
                #print 'startet nytt bfs'
                besokte_kanter += nye_kanter
                besokte_noder += nye_noder
        index += 1
    return besokte_kanter, besokte_noder




def main():
    n = int(stdin.readline())
    antall_kanter = 0
    nabomatrise = [None] * n  # rader == Her begynner nodene
    for i in range(0, n):
        nabomatrise[i] = [False] * n  # kolonner
        linje = stdin.readline()
        for j in range(0, n):
            if linje[j] == '1':
                nabomatrise[i][j] = '1'
                antall_kanter += 1
            else:
                nabomatrise[i][j] = '0'
    for linje in stdin:
        start = int(linje)
        print "%.3f" % (subgraftetthet(nabomatrise, start, antall_kanter) + 1E-12)

main()
