__author__ = 'Vemund'

from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    # SKRIV DIN KODE HER
    pass


def posisjoner(ord, indeks, node):
    # SKRIV DIN KODE HER
    pass


def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append( (o,pos) )
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print sokeord + ":",
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print p,
            print
    except:
        traceback.print_exc(file=stderr)
main()