# https://projecteuler.net/problem=15
# This is essentially: https://leetcode.com/problems/unique-paths/


if __name__ == '__main__':

    try:

        def init(num):
            lattice = []

            # A 2 x 2 lattice should be represented as a 3 x 3 grid.
            # A 1 x 1 lattice should be represented as a 2 x 2 grid.
            for r in range(0,num+1,1):
                row = []
                for c in range(0,num+1,1):
                    row.append(0)

                lattice.append(row)

            print(lattice)
            return lattice

        # init(1)
        # init(2)
        # init(20)

        def solve(lattice):
            LEN = len(lattice)

            for r in range(0,LEN,1):
                for c in range(0,LEN,1):
                    if (r == 0):
                        lattice[r][c] = 1
                    else:
                        if (r > 0):
                            lattice[r][c] += lattice[r-1][c]
                        if (c > 0):
                            lattice[r][c] += lattice[r][c-1]

            print(lattice)
            return lattice[LEN - 1][LEN - 1]
            
        solve(init(20))

        # solve(init(2))

        # 1
        # [
        #   [1, 1], 
        #   [1, 2]
        # ]

        # 2
        # [
        #   [1, 1, 1], 
        #   [1, 2, 3], 
        #   [1, 3, 6]
        # ]

    except Exception as ex:

        print('Exception: ' + str(ex))