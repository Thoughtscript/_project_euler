# https://projecteuler.net/problem=34

if __name__ == '__main__':

    try:

        MAPPINGS = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 6,
            "4": 24,
            "5": 120,
            "6": 720,
            "7": 5040,
            "8": 40320,
            "9": 362880
        }

        def solve():
            sum = 0

            for x in range(29999999, 199999999, 1):
                s = str(x)
                inner_sum = 0
                for y in range(0, len(s), 1):
                    inner_sum += MAPPINGS.get(s[y])

                if inner_sum == x and x >= 3:
                    print("Digital factorial found: " + str(x))
                    sum += x

            print(sum)
            return sum

        # 145 is the only number below 9999999
        # none to 19999999
        # none to 29999999
        solve()

        def test(x):
            sum = 0
            s = str(x)
            inner_sum = 0
            for y in range(0, len(s), 1):
                inner_sum += MAPPINGS.get(s[y])

            if inner_sum == x and x != 1 and x != 2:
                print("Digital factorial found: " + str(x))
                sum += x

            print(sum)
            return sum

        # test(9999900)

    except Exception as ex:

        print('Exception: ' + str(ex))