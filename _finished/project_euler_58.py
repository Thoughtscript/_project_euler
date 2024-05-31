# https://projecteuler.net/problem=58

# Better analysis 
## My own original analysis to simplify by just generating the diags!!!!

# [65, 64, 63, 62, 61, 60, 59, 58, 57], 
# [66, 37, 36, 35, 34, 33, 32, 31, 56], 
# [67, 38, 17, 16, 15, 14, 13, 30, 55], 
# [68, 39, 18, 5, 4, 3, 12, 29, 54], 
# [69, 40, 19, 6, 1, 2, 11, 28, 53], 
# [70, 41, 20, 7, 8, 9, 10, 27, 52], 
# [71, 42, 21, 22, 23, 24, 25, 26, 51], 
# [72, 43, 44, 45, 46, 47, 48, 49, 50],
# [73, 74, 75, 76, 77, 78, 79, 80, 81]

# [37, 36, 35, 34, 33, 32, 31], 
# [38, 17, 16, 15, 14, 13, 30], 
# [39, 18, 5, 4, 3, 12, 29], 
# [40, 19, 6, 1, 2, 11, 28], 
# [41, 20, 7, 8, 9, 10, 27], 
# [42, 21, 22, 23, 24, 25, 26], 
# [43, 44, 45, 46, 47, 48, 49]

# [17, 16, 15, 14, 13],
# [18, 5, 4, 3, 12], 
# [19, 6, 1, 2, 11], 
# [20, 7, 8, 9, 10], 
# [21, 22, 23, 24, 25]

# UR: 1, 3, 13, 31, 57
##      2, 10, 18, 26 -> increases by 8 (2nd Order Derivative)
# UL: 1, 5, 17, 37, 65
##      4  12  20  28 -> increases by 8 (2nd Order Derivative)
# LL: 1, 7, 21, 43, 73
##      6  14  22  30 -> increases by 8 (2nd Order Derivative)
# LR: 1, 9, 25, 49, 81
##      8  16  24  32 -> increases by 8 (2nd Order Derivative)

import time

if __name__ == '__main__':

    try:   
        # Generate an 0-indexed array where:
        # sieve[i] = False indicates non-prime
        # sieve[i] = True indicates prime
        def sieve_of_eratosthenes(num):
            sieve = [0] * num
            sieve[0] = False

            for x in range(2, num+1, 1):
                if sieve[x-1] is 0:
                    sieve[x-1] = True

                for y in range(x*2, num+1, x):
                    sieve[y-1] = False

            return sieve

        def map_num_to_arr(sieve):
            primes = []

            for x in range(0, len(sieve), 1):
                if sieve[x] == True:
                    primes.append(x+1)

            return primes

        def prime_map(num):
            BEGIN = time.time()

            primes = map_num_to_arr(sieve_of_eratosthenes(num))
            prime_map = {}

            for x in range(0, len(primes), 1):
                prime_map[primes[x]] = True

            END = time.time()
            print("Primes up to " + str(num) + " generated in: " + str(END-BEGIN)) # Primes up to 690000000 generated in: 740.1217658519745
            # Can pregenerate this - if so the below solution is nearly instantaneous
            # File size would likely be ovover 250 MB so programmatically do so for now
            
            return prime_map
        
        PRIME_MAP = prime_map(690_000_000)

        def is_prime(x):
            return not PRIME_MAP.get(x) is None
                
        # Vastly streamlined this in terms of memory, etc.
        def solve():
            ALGO_BEGIN = time.time()

            # delta ul, delta ll, etc.
            dul, dll, dlr, dur = [12, 14, 16, 10]
            # next ul, next ll
            nul, nll, nlr, nur = [17, 21, 25, 13]
            # primes, non-primes
            ps, nps = [5, 4]
            side_length = 5

            for layer in range(0, 999_999_999, 1):
                print("Layer " + str(layer))

                dul += 8
                dll += 8
                dlr += 8
                dur += 8

                nul += dul
                nll += dll
                nlr += dlr
                nur += dur

                side_length += 2
                print("side_length: " + str(side_length) + " added: " + str([nul, nll, nlr, nur]))
                
                if not is_prime(nul):
                    nps += 1
                else:
                    ps += 1

                if not is_prime(nlr):
                    nps += 1
                else:
                    ps += 1

                if not is_prime(nll):
                    nps += 1
                else:
                    ps += 1

                if not is_prime(nur):
                    nps += 1
                else:
                    ps += 1

                percent = ps / (ps + nps)
                print("count_primes " + str(ps) + " count_non_primes " + str(nps) + " % " + str(percent))

                if percent < .1:
                    print("Solution found at layer: " + str(layer) + " with side_length: " + str(side_length))
                    ALGO_END = time.time()
                    print("Solution found in: " + str(ALGO_END-ALGO_BEGIN))
                    break
        
        solve() 

        # side_length: 26241 added: [688537601, 688563841, 688590081, 688511361]
        # count_primes 5248 count_non_primes 47233 % 0.09999809454850327
        # Solution found at layer: 13117 with side_length: 26241
        # Solution found in: 0.3020131587982178

    except Exception as ex:

        print('Exception: ' + str(ex))