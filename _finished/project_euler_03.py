# https://projecteuler.net/problem=3

import primes_to_2mil

if __name__ == '__main__':

    try:

        # So, the target number is: 600851475143:
        #
        # The minimum division case (besides 1) is NUM / 2.
        # 300,425,737,571.5 and that doesn't divide cleanly.
        # Nor does 3.
        #
        # First, determine the minimum division case.
        # This will help to determine the least highest upper bound of primes.
        # I suspect that this may be a large number so it'll help to narrow down 
        # the primes that should be considered.

        # ---------------------------------------- #

        def first_clean_divide(num,lim):
            print("Finding first clean divide for " + str(num))
            result = []
            for x in range(2,lim):
                # print("Dividing by " + str(x))
                if num % x == 0:
                   # print(x)
                   result.append(x)
                   result.append(num / x)
                   # return x

            result.sort()
            print(result)

        # first_clean_divide(600851475143,100000000)
        # [71, 839, 1471, 6857, 6857, 59569, 59569, 104441, 104441, 486847, 486847, 1234169, 1234169, 5753023, 5753023, 10086647, 10086647, 87625999, 87625999, 408464633, 716151937, 8462696833]

        # ---------------------------------------- #

        def solve():
            primes = primes_to_2mil.primes
            for x in primes:
                if 600851475143 % x == 0:
                    print(x)

        solve()

        def find_in_primes(arr):
            primes = primes_to_2mil.primes
            arr.reverse()
            for x in arr:
                if x in primes:
                    print(x)
                    return x

        find_in_primes([71, 71, 839, 839, 1471, 1471, 6857, 6857, 59569, 59569, 104441, 104441, 486847, 486847, 1234169, 1234169, 5753023, 5753023, 10086647, 10086647, 87625999, 87625999, 408464633, 408464633, 716151937, 716151937,8462696833, 8462696833])


    except Exception as ex:

        print('Exception: ' + str(ex))