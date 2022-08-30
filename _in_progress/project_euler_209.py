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
       # Therefore 2^7 total arrays generated (64 distinct and mutually exclusive pairs)
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
                            mututally_exl = True
                            for z in range(0, len(rows[x]) - 1, 1):
                                if not rows[x][z] == rows[y][z]:
                                    mututally_exl = False
                                    break

                            if not mututally_exl:
                                count += 1
                                print("Row match found: " + str(rows[x]) + " " + str(rows[y]))

            # 128 distinct rows can be generated.
            # Each 6 variable input truth-table has 2^6 rows (64 total).
            # Each match finds 2 rows and excludes 2 other options (since 64 / 128 total are mutually exclusive with the other option).
            # So, there are 2^6 rows - 2 remaining (62) and 124 remaining distinct combinations.
            # For each of the remaining 62 rows, there are 2 possible truth assignments.

            print("Matches found: " + str(count)) # 189
            table_rows_left = pow(2, 6) - 2
            print("Table rows remaining: " + str(table_rows_left)) # 62
            table_combos = pow(2, table_rows_left)
            print("Combinations per table found: " + str(table_combos)) # 4611686018427387904
            result = count * table_combos
            print("Total combinations found: " + str(result)) # 871608657482776313856

            # Think the answer is strictly less than 871608657482776313856
            # Specifically strictly matches are less than 189 since some matches can be in the same table.
            return result

        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))
