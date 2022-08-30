# https://projecteuler.net/problem=345
import copy

if __name__ == '__main__':

    try:

        matrix = [
            [7, 53, 183, 439, 863, 497, 383, 563, 79, 973, 287, 63, 343, 169, 583],
            [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
            [447, 283, 463, 29, 23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
            [217, 623, 3, 399, 853, 407, 103, 983, 89, 463, 290, 516, 212, 462, 350],
            [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
            [870, 456, 192, 162, 593, 473, 915, 45, 989, 873, 823, 965, 425, 329, 803],
            [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
            [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601, 95, 973],
            [445, 721, 11, 525, 473, 65, 511, 164, 138, 672, 18, 428, 154, 448, 848],
            [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
            [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
            [821, 461, 843, 513, 17, 901, 711, 993, 293, 157, 274, 94, 192, 156, 574],
            [34, 124, 4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
            [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
            [813, 883, 451, 509, 615, 77, 281, 613, 459, 205, 380, 274, 302, 35, 805]
        ]

        ROWS = len(matrix)
        COLS = len(matrix[0])

        def make_cols():
            cols = []

            for c in range(0, len(matrix), 1):
                col = []

                for r in range(0, len(matrix), 1):
                    col.append(matrix[r][c])

                cols.append(col)
                # print(col)

            # print(cols)
            return cols

        def generate_perms():
            perms = []
            # fh = open("permutations.txt", "a")

            for a in range(0, ROWS, 1):
                tempa = {}
                tempa[a] = 1

                for b in range(0, ROWS, 1):
                    tempb = copy.deepcopy(tempa)
                    if not tempb.get(b) == None:
                        continue
                    tempb[b] = 1

                    for c in range(0, ROWS, 1):
                        tempc = copy.deepcopy(tempb)
                        if not tempc.get(c) == None:
                            continue
                        tempc[c] = 1

                        for d in range(0, ROWS, 1):
                            tempd = copy.deepcopy(tempc)
                            if not tempd.get(d) == None:
                                continue
                            tempd[d] = 1

                            for e in range(0, ROWS, 1):
                                tempe = copy.deepcopy(tempd)
                                if not tempe.get(e) == None:
                                    continue
                                tempe[e] = 1

                                for f in range(0, ROWS, 1):
                                    tempf = copy.deepcopy(tempe)
                                    if not tempf.get(f) == None:
                                        continue
                                    tempf[f] = 1

                                    for g in range(0, ROWS, 1):
                                        tempg = copy.deepcopy(tempf)
                                        if not tempg.get(g) == None:
                                            continue
                                        tempg[g] = 1

                                        for h in range(0, ROWS, 1):
                                            temph = copy.deepcopy(tempg)
                                            if not temph.get(h) == None:
                                                continue
                                            temph[h] = 1

                                            for i in range(0, ROWS, 1):
                                                tempi = copy.deepcopy(temph)
                                                if not tempi.get(i) == None:
                                                    continue
                                                tempi[i] = 1

                                                for j in range(0, ROWS, 1):
                                                    tempj = copy.deepcopy(tempi)
                                                    if not tempj.get(j) == None:
                                                        continue
                                                    tempj[j] = 1

                                                    for k in range(0, ROWS, 1):
                                                        tempk = copy.deepcopy(tempj)
                                                        if not tempk.get(k) == None:
                                                            continue
                                                        tempk[k] = 1

                                                        for l in range(0, ROWS, 1):
                                                            templ = copy.deepcopy(tempk)
                                                            if not templ.get(l) == None:
                                                                continue
                                                            templ[l] = 1

                                                            for m in range(0, ROWS, 1):
                                                                tempm = copy.deepcopy(templ)
                                                                if not tempm.get(m) == None:
                                                                    continue
                                                                tempm[m] = 1

                                                                for n in range(0, ROWS, 1):
                                                                    tempn = copy.deepcopy(tempm)
                                                                    if not tempn.get(n) == None:
                                                                        continue
                                                                    tempn[n] = 1

                                                                    for o in range(0, ROWS, 1):
                                                                        tempo = copy.deepcopy(tempn)
                                                                        if not tempo.get(o) == None:
                                                                            continue

                                                                        # print([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o])
                                                                        # fh.write(str([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]) + "\n")
                                                                        perms.append([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o])
                                                                        

            # fh.close()
            # print(perms)
            return perms

        def solve():
            cols = make_cols()
            perms = generate_perms()
            mx = 0

            for x in range(0, len(perms), 1):
                sum = 0

                for y in range(0, len(perms[x]), 1):
                    sum += cols[y][perms[x][y]]

                if (sum < mx):
                    print("New max found: " + str(sum))
                    print("Matrix sum " + str(perms[x]))
                    mx = sum

            print(mx)
            return mx

        solve()

        # Three ways:

        # i. Factorial brute force - permutations - too slow.
        # ii. (Pre-)sort each row and then col by sorted rows.
        # iii. Solve upper-right to lower-left expanding the matrix sum from n to m (n < m)?

    except Exception as ex:

        print('Exception: ' + str(ex))
