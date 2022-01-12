# https://projecteuler.net/problem=45

if __name__ == '__main__':

    try:

        def make_triangle_nums(mx):
            result = {}
            for x in range(1, mx, 1):
                num = x * (x + 1) / 2
                result[num] = num

            return result

        def make_pentagonal_nums(mx):
            result = {}
            for x in range(1, mx, 1):
                num = x * (3 * x - 1) / 2
                result[num] = num

            return result

        def make_hexagonal_nums(mx):
            result = {}
            for x in range(1, mx, 1):
                num = x * (2 * x - 1)
                result[num] = num

            return result

        def solve(mx):
            tri_map = make_triangle_nums(mx)
            pentagonal_map = make_pentagonal_nums(mx)
            hexagonal_map = make_hexagonal_nums(mx)

            TRI_VALS = tri_map.values()
            LEN_TRI_VALS = len(TRI_VALS)

            for x in range(1, LEN_TRI_VALS, 1):
                A = TRI_VALS[x]
                B = pentagonal_map.get(A)
                C = hexagonal_map.get(A)

                if B is None or C is None:
                    continue

                print("Number found: " + str(A))

                if A > 40755:
                    print("Next highest number found " + str(A))
                    return A

            return

        solve(100000) # 1533776805

    except Exception as ex:

        print('Exception: ' + str(ex))