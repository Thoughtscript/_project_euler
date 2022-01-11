# https://projecteuler.net/problem=29

if __name__ == '__main__':

    try:

        def solve():
            hm = {}

            for x in range(0, 101,1):
                for y in range(0, 101, 1):
                    val = pow(x, y)
                    hm[val] = True

            result = len(hm.values())
            print(str(result) + " distinct values")
            return result

        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))