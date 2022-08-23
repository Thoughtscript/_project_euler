# https://projecteuler.net/problem=34

if __name__ == '__main__':

    try:
        # 0! is 1 = ARGGGGGGGGGGGGGGGGGGGGGGGGG!!!!!!!!!!!!!!!!!
        MAPPINGS = {
            "0": 1,
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

            for x in range(0, 999999999, 1):
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

        solve() # 40730
        # 0! = 1 duh not 0
        # No numbers are valid below 0
        # 1! and 2! aren't counted

        # See: https://mathworld.wolfram.com/Factorion.html

    except Exception as ex:

        print('Exception: ' + str(ex))