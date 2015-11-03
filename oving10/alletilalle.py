def main():
    from sys import stdin

    maxint = 3500
    testcases = int(stdin.readline())
    for test in range(testcases):
        byer = int(stdin.readline())
        rekkefolge = map(int, stdin.readline().split())
        rekkefolge.append(rekkefolge[0])
        nabomatrise = [map(lambda x: maxint if x == '-1' else int(x), stdin.readline().split()) for _ in range(byer)]

        for k in range(byer):
            for i in range(byer):
                for j in range(byer):
                    nabomatrise[i][j] = min(nabomatrise[i][j], nabomatrise[i][k] + nabomatrise[k][j])
        rute = 0
        current = rekkefolge[0]
        umulig = False
        for by in rekkefolge[1:]:
            vei = nabomatrise[current][by]
            if vei == maxint:
                umulig = True
                break
            rute += vei
            current = by
        if umulig:
            print 'umulig'
        else:
            print rute
main()
