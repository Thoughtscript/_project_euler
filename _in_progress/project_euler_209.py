# https://projecteuler.net/problem=209

if __name__ == '__main__':

    try:

        def xor(x, y):
            if (x == 0 and y == 0):
                return 0
            if (x == 0 and y == 1):
                return 1
            if (x == 1 and y == 0):
                return 1
            if (x == 1 and y == 1):
                return 0

        # Here since we're defining a meta-linguistic construct 
        # otherwise can just use and (... e.g. for clarity)
        def nd(x, y):
            if (x == 0 and y == 0):
                return 0
            if (x == 0 and y == 1):
                return 0
            if (x == 1 and y == 0):
                return 0
            if (x == 1 and y == 1):
                return 1       
       
        def generate_rows():
            rows = []

            for a in range(0,2,1):
                for b in range(0,2,1):
                    for c in range(0,2,1):
                        for d in range(0,2,1):
                            for e in range(0,2,1):
                                for f in range(0,2,1):
                                    for g in range(0,2,1):
                                        rows.append([a,b,c,d,e,f,g])
            
            return rows
        
        def solve():
            count = 0

            rows = generate_rows()

            print(str(len(rows)) + " Total Rows Found")

            for x in range(0, len(rows), 1):

                a = rows[x][0]
                b = rows[x][1]
                c = rows[x][2]
                d = rows[x][3]
                e = rows[x][4]
                f = rows[x][5]

                xx = xor(a, nd(b, c))

                for y in range(0, len(rows), 1):
                    if b == rows[y][0] and c == rows[y][1] and d == rows[y][2] and e == rows[y][3] and f == rows[y][4] and xx == rows[y][5]:
                        if nd(rows[x][6], rows[y][6]) == 0:
                            count += 1
                            print("Row match found: " + str(rows[x]) + " " + str(rows[y]))

            # Need to compute the permutations of the above...
            # E.g. - Row match found: [1, 1, 0, 1, 1, 0, 0] [1, 0, 1, 1, 0, 1, 1]

            # [
            #   [1, 1, 0, 1, 1, 0, 0]
            #   [1, 0, 1, 1, 0, 1, 1]
            #   ...
            #   ...
            #   ...
            #   ...
            # ]

            # Think it's 126 x 125 x 124 x 123 x count
            result = 126 * 125 * 124 * 123 * count
            print(result)
            return result

        solve() # 46122048000

    except Exception as ex:

        print('Exception: ' + str(ex))
