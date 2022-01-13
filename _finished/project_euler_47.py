# https://projecteuler.net/problem=47

import primes_to_2mil as P

if __name__ == '__main__':

    try:

        def prime_map():
            primes = {}

            for x in range(0, len(P.primes), 1):
                primes[P.primes[x]] = True
            
            return primes

        PRIME_MAP = prime_map()

        def check_prime(num):
            SQ_RT = pow(num, 1/2)

            for x in range(2, SQ_RT+1, 1):
                if num % x == 0:
                    return False

            return True

         # Offset num by one when accessing
        
        def prime_factorization(num):
            result = []
            rem = num

            while rem % 2 == 0:
                rem = rem / 2
                result.append(2)

            # Must be odd or not divisible by 2 once it reaches here
            for x in range(3, num+1, 2):
                if PRIME_MAP.get(x) is None and x <= 1999993:
                    continue

                if x > 1999993 and not check_prime(x):
                    continue

                while (rem % x == 0):
                    result.append(x)
                    rem = rem / x

                if rem == 1 or rem == 0:
                    break
            
            # print(result)
            return result

        def number_of_divisors(num):
            prime_factors = prime_factorization(num)
            hm = {}

            for x in range(0, len(prime_factors), 1):
                n = prime_factors[x]

                if not hm.get(n) is None:
                    hm[n] = hm[n] + 1
                else:
                    hm[n] = 1

            return len(hm.keys())

        def solve(known_above):

            for x in range(1, 999999, 1):
                if x < known_above:
                    continue

                A = x
                B = x + 1
                C = x + 2
                D = x + 3

                print("Trying: " + str(A) + " " + str(B) + " " + str(C) + " " + str(D))

                NUM_A = number_of_divisors(A)
                if not NUM_A == 4:
                    continue

                NUM_B = number_of_divisors(B)
                if not NUM_B == 4:
                    continue

                NUM_C = number_of_divisors(C)
                if not NUM_C == 4:
                    continue

                NUM_D = number_of_divisors(D)
                if not NUM_D == 4:
                    continue

                if NUM_A == 4 and NUM_B == 4 and NUM_C == 4 and NUM_D == 4:
                    print("First four consecutive integers found with at least four distinct prime factors!")
                    print(str(A))
                    return A
            
            print("None found!")
            return

        solve(134035) # > 134035

        # Solution: 134043

    except Exception as ex:

        print('Exception: ' + str(ex))