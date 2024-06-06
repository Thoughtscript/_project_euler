# https://projecteuler.net/problem=243

from decimal import *
import primes_to_2mil as PRIMES

if __name__ == '__main__':

    try:

        def prime_map():
            primes = {}

            for x in range(0, len(PRIMES.primes), 1):
                primes[PRIMES.primes[x]] = True
            
            # print(primes)
            return primes

        PRIME_MAP = prime_map()

         # Offset num by one when accessing
        
        def prime_factorization(num, pfs):
            # map deduplicates - don't check 2^3 3 times say
            map = {}
            rem = num

            while rem % 2 == 0:
                rem = rem / 2
                map[2] = True

            # Must be odd or not divisible by 2 once it reaches here
            for x in range(3, num+1, 2):
                if PRIME_MAP.get(x) is None:
                    continue

                while (rem % x == 0):
                    map[x] = True
                    rem = rem / x

                if rem == 1 or rem == 0:
                    break

            pfs[num] = map
            return map
        
        # Every num can be put into prime factorization
        # If a num and denom don't share any prime factors, it's already proper
        #
        # The total distinct number of prime factors is relatively small 
        # so this is much faster than checking by GCD.
        def is_resilient_proper_fraction(n, dmap, pfs):
            nn = pfs.get(n)
            if nn is None:
                nn = prime_factorization(n, pfs)
                pfs[n] = nn
            
            nn = list(nn.keys())
                
            for x in range(0, len(nn), 1):
                if not dmap.get(nn[x]) is None:
                    return False
                
            return True      

        def solve(mn_num, mx_num):
            target = Decimal(15499) / Decimal(94744)

            # cache/memoize prime factors for the numerators and denom
            pfs = {}

            for d in range(mn_num, mx_num+1, 1):
                print(str(d))
                resilient = 0
                non_resilient = 0

                if not PRIME_MAP.get(d) is None:
                    # print("Prime d: " + str(d) + " found - skipping as ratio: 1/1 ...")
                    continue

                # Maximum number of resilient that can be encountered at d
                inner_target = Decimal(target) * Decimal(d)

                dmap = prime_factorization(d, pfs)
                
                for n in range(1, d, 1):
                    if is_resilient_proper_fraction(n, dmap, pfs):
                        resilient += 1
                    else:
                        non_resilient += 1

                    if Decimal(resilient) > inner_target:
                        # print("Breaking early for d: " + str(d ) + " as ratio target exceeded...")
                        break
                
                ratio = Decimal(resilient) / Decimal(resilient + non_resilient)
                if ratio < target:
                    print("Solution found for d: " + str(d))
                    return d
                    
            print("No solution found!")

        # solve(1_079_651, 2_000_000)
        solve(145_963, 2_000_000)
                         
    except Exception as ex:

        print('Exception: ' + str(ex))