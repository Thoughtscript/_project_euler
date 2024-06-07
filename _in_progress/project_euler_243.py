# https://projecteuler.net/problem=243

from decimal import *
import primes_to_50_mil as PRIMES

if __name__ == '__main__':

    try:
        MAX_PRIME = 50_000_000

        def prime_map():
            primes = {}

            for x in range(0, len(PRIMES.primes), 1):
                primes[PRIMES.primes[x]] = True
            
            return primes

        PRIME_MAP = prime_map()

        def check_prime(num):
            SQ_RT = pow(num, 1/2)

            for x in range(2, SQ_RT+1, 1):
                if num % x == 0:
                    return False

            return True

        # Technique from: https://www.geeksforgeeks.org/python-merging-two-dictionaries/
        def Merge(dict1, dict2):
            merged = {**dict1, **dict2}
            return merged

        def prime_factorization(num, pfs_memo):
            # map deduplicates - don't check 2^3 3 times say
            map = {}
            rem = num

            while rem % 2 == 0:
                rem = rem / 2
                check_memo = pfs_memo.get(rem)
                if not check_memo is None:
                    merged = Merge(map, check_memo)
                    pfs_memo[num] = merged
                    return list(merged.keys())

                map[2] = True

            # Must be odd or not divisible by 2 once it reaches here
            for x in range(3, num+1, 2):
                if PRIME_MAP.get(x) is None and x <= MAX_PRIME:
                    continue

                if x > MAX_PRIME and not check_prime(x):
                    continue

                while (rem % x == 0):
                    map[x] = True
                    rem = rem / x
                    check_memo = pfs_memo.get(rem)
                    if not check_memo is None:
                        merged = Merge(map, check_memo)
                        pfs_memo[num] = merged
                        return list(merged.keys())

                if rem == 1 or rem == 0:
                    break

            pfs_memo[num] = map
            return list(map.keys())

        # https://cp-algorithms.com/algebra/phi-function.html
        ## I was just introduced to this technique
        ## the approach below combines my first approach with it
        ### Also, it removes a loop time-complexity-wise
        def euler_totient_fun(n, pfs_memo):
            # get prime factors of n, not the exponents
            pfs = prime_factorization(n, pfs_memo)
            result = Decimal(n)

            # n * (1-(1/pfs[0])) * (1-(1/pfs[1])) ... 
            for x in range(0, len(pfs), 1):
                pf = Decimal(pfs[x])
                result *= Decimal(Decimal(1) - (Decimal(1)/pf))

            return result
        
        '''
        def unit_test():
            answers = {
                1: 1,
                2: 1,
                3: 2,
                4: 2,
                5: 4,
                6: 2,
                7: 6,
                8: 4,
                9: 6,
                10: 4,
                11: 10,
                12: 4,
                13: 12,
                14: 6,
                15: 8,
                16: 8,
                17: 16,
                18: 6,
                19: 18,
                20: 8,
                21: 12
            }

            for x in range(1, 22, 1):
                expected = answers.get(x)
                actual = euler_totient_fun(x)
                if not actual == expected:
                    print("Error for x: " + str(x) + " actual " + str(actual) + " expected " + str(expected))
        
        unit_test()
        '''

        def solve(min_num, max_num):
            # Memoize each rem and pfs for each num
            ## since I drop the exponents
            pfs_memo = {}
            target = Decimal(15499) / Decimal(94744)

            for denom in range(min_num, max_num, 1):
                print("Trying d: " + str(denom))

                # I previously observed that no prime denom will have a ratio less than 100%
                ## Also see the above: a prime P will have P-1/P-1 ratio.
                if not PRIME_MAP.get(denom) is None and denom <= MAX_PRIME:
                    print("Prime d: " + str(denom) + " found - skipping as ratio: 1/1 ...")
                    continue

                # if denom > MAX_PRIME and not check_prime(denom):
                #     print("Prime d: " + str(denom) + " found - skipping as ratio: 1/1 ...")
                #     continue

                '''
                # This analytically computes all relative coprimes w.r.t to denom
                ## Each relative coprimes is less than denom and doesn't have a GCD other than 1 w.r.t to denom
                
                As such, each computed answer is the sum of all resilient fractions for denom:
                I. proper -> num < denom 
                II. num / denom is already maximally reduced 
                '''
                num = euler_totient_fun(denom, pfs_memo)

                ratio = Decimal(num) / Decimal(denom - 1)
                if ratio < target:
                    print("Solution found for d: " + str(denom))

            print("No solution found!")

        solve(6_873_571, 999_999_999)
                                         
    except Exception as ex:

        print('Exception: ' + str(ex))