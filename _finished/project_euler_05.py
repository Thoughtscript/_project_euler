# https://projecteuler.net/problem=5

if __name__ == '__main__':

    try:
        def determine_max(top):
            if top <= 10:
                print("Please supply an input gt 10")
                return

            result = 2520

            for x in range(11,top+1,1):
                result = result * x

            print(result)
            return result

        # determine_max(20) # 1689515283456000

        # Number must be even since it must be cleanly divisible by 2.
        # Must end in a 0 since it must be cleanly divisible by 2, 5, 10, and 20.

        def solve():
            for x in range(2520,1000000000,1):

                if not x % 2 == 0:
                    continue
                if not x % 3 == 0:
                    continue
                if not x % 4 == 0:
                    continue
                if not x % 5 == 0:
                    continue
                if not x % 6 == 0:
                    continue
                if not x % 7 == 0:
                    continue
                if not x % 8 == 0:
                    continue
                if not x % 9 == 0:
                    continue
                if not x % 10 == 0:
                    continue
                if not x % 11 == 0:
                    continue
                if not x % 12 == 0:
                    continue
                if not x % 13 == 0:
                    continue
                if not x % 14 == 0:
                    continue
                if not x % 15 == 0:
                    continue
                if not x % 16 == 0:
                    continue
                if not x % 17 == 0:
                    continue
                if not x % 18 == 0:
                    continue
                if not x % 19 == 0:
                    continue
                if not x % 20 == 0:
                    continue

                print(x)
                return x
            
            print("No answer found!")
            return

        solve() # 232792560

    except Exception as ex:
        print('Exception: ' + str(ex))