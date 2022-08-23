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

            for x in range(-999, 0, 1):
                s = str(x)
                inner_sum = 0
                first = True
                for y in range(0, len(s), 1):
                    if s[y] == "-":
                        continue

                    digit = MAPPINGS.get(s[y])
                    if first and x < 0:
                        inner_sum -= MAPPINGS.get(s[y])
                    else:
                        inner_sum += MAPPINGS.get(s[y])
                    first = False

                print("Attempting " + str(inner_sum) + " for " + s)
                if inner_sum == x:
                    print("Digital factorial found: " + str(x))
                    sum += x

            print(sum)
            return sum

        # 145 is the only number below 9999999
        # none to 19999999
        # none to 29999999

        # try negative numbers
        solve()

        def test(x):
            sum = 0
            s = str(x)
            inner_sum = 0
            first = True
            for y in range(0, len(s), 1):
                if s[y] == "-":
                    continue

                digit = MAPPINGS.get(s[y])
                if first and x < 0:
                    inner_sum -= MAPPINGS.get(s[y])
                else:
                    inner_sum += MAPPINGS.get(s[y])
                first = False

            if inner_sum == x:
                print("Digital factorial found: " + str(x))
                sum += x

            print(sum)
            return sum

        # test(9999900)

    except Exception as ex:

        print('Exception: ' + str(ex))