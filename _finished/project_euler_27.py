# https://projecteuler.net/problem=27

import math

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

        PRIMES = map_num_to_arr(sieve_of_eratosthenes(100000))

        def prime_map():
            primes = {}

            for x in range(0, len(PRIMES), 1):
                primes[PRIMES[x]] = True
            
            return primes

        PRIME_MAP = prime_map()

        def check_prime(num):
            if PRIME_MAP.get(num) is None:
                return False

            return True

        def formula(n, a, b):
            return math.pow(n, 2) + a * n + b

        def solve():
            mx = 0
            coefficient_prod = 0

            for a in range(-999, 999, 1):
                for b in range(-1000, 1001, 1):
                    seq_len = 0
                    for n in range(0, 81, 1):
                        formula_out = formula(n, a, b)
                        if check_prime(formula_out):
                            seq_len += 1
                        else:
                            mx = max(seq_len, mx)
                            if seq_len == mx:
                                coefficient_prod = a * b
                                print("New max sequence found! " + str(seq_len) + " with coefficient " + str(coefficient_prod) + " a " + str(a) + " b " + str(b))
                            break

            print("Result found: " + str(coefficient_prod))
            return coefficient_prod

        solve() # -59231

        def test():
            for a in range(-100, 0, 1):
                for b in range(1000, 2000, 1):
                    temp = 0
                    for n in range(0, 81, 1):
                        formula_out = formula(n, a, b)
                        if check_prime(formula_out):
                            temp += 1
                        else:
                            if temp > 10:
                                print("New sequence found! " + str(temp) + " with coefficient " + str(a * b) + " a " + str(a) + " b " + str(b))
                            break

       # test() # New sequence found! 80 with coefficient -126479 a -79 b 1601

    except Exception as ex:

        print('Exception: ' + str(ex))