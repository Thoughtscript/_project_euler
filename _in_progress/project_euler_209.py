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
       
       # 2^6 total distinct rows
       # Each of the 64 total distinct rows can also be assigned a 0 or a 1
       # Therefore 2^7 total arrays generated
        def generate_rows():
            rows = []

            for a in range(0,2,1):
                for b in range(0,2,1):
                    for c in range(0,2,1):
                        for d in range(0,2,1):
                            for e in range(0,2,1):
                                for f in range(0,2,1):

                                    # This is the truth-assignment to the rest of the row
                                    # Truth in this form for 'nd'/'and' would be [[1, 1, 1], [0, 0, 0], [1, 0, 0], [0, 1, 0]]
                                    for g in range(0,2,1):
                                        rows.append([a,b,c,d,e,f,g])
            
            return rows
        
        def solve():
            count = 0

            rows = generate_rows()

            print(str(len(rows)) + " Total Unique Rows Found")
            print(rows)

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

            # Note that each row must be distinct in a truth-table.
            # Consider the following made up operator 'zx'
            #
            # | a b c | zx(a, b, c) |
            # | ----- | ----------- |
            # | 1 1 1 | 1           |
            # | 1 0 1 | 1           |
            # | 0 0 1 | 0           |
            # | ...   |             |
            #
            # 2^3 distinct rows for boolean and 2^4 total rows with truth-assignments

            # So, given two matching rows, how many total tables can those two rows belong to?
            # Think it's count * (128 - 2 * 2) * (128 - 2 * 2 - 2) * (128 - 2 * 2 - 4) * (128 - 2 * 2 - 6) * (128 - 2 * 2 - 8)

            # Consider again the above:
            # [[1, 1, 1], [0, 0, 0], [1, 0, 0], [0, 1, 0]]
            # [1, 1, 1], [0, 0, 0] can be combined with [1, 0, 0], [0, 1, 0], [1, 0, 1], [0, 1, 1]
            # forming 2 distinct tables or 2 x 1 x count where count - 1
            # ...
            # The 2 comes from 4 - 2
            # The 4 comes 2^3 total rows with truth assignments
            # 2 ([1, 1, 0], [0, 0, 1]) are mutually exclusive with the other 2: [1, 1, 1], [0, 0, 0]
            # So, 2^3 - 4 - 2

            # Note too that each row randomly selected actually removes both it and its mutually exclusive row!

            result = count * (128 - 2 * 2) * (128 - 2 * 2 - 2) * (128 - 2 * 2 - 4) * (128 - 2 * 2 - 6) * (128 - 2 * 2 - 8)
            print(result)
            return result

        solve() # 4770940354560

    except Exception as ex:

        print('Exception: ' + str(ex))
