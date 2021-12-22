# https://projecteuler.net/problem=12

import primes_to_2mil as PRIMES

if __name__ == '__main__':

    try:

        def prime_map():
            primes = {}

            for x in range(0, len(PRIMES.primes), 1):
                primes[PRIMES.primes[x]] = True
            
            print(primes)
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
            result = 1
            hm = {}

            for x in range(0, len(prime_factors), 1):
                n = prime_factors[x]

                if not hm.get(n) is None:
                    hm[n] = hm[n] + 1
                else:
                    hm[n] = 1

            keys = hm.keys()
            
            for x in range(0, len(keys), 1):
                n = hm[keys[x]]
                result = result * (n + 1)

            # print(result)
            return result

        # Generates all triangular numbers up to num.
        def generate(num):
            arr = []
            last = 0
            for x in range(1,num+1,1):
                y = x + last
                last = y
                arr.append(y)

            # print(arr)
            return arr

        # ------------------------------------- #

        def solve(num):
            # Cache these so they aren't repeatedly generated.
            triangulars = generate(num)
            num_with_most_factors = 1
            most_factors = 1

            for x in range(0, len(triangulars),1):
                TRI_NUM = triangulars[x]
                factors = number_of_divisors(TRI_NUM)
                print("Triangular Number: " + str(TRI_NUM) + " has number of factors: " + str(factors))

                if factors > most_factors:
                    most_factors = factors
                    num_with_most_factors = TRI_NUM
                    print("New largest num. of factors found: " + str(num_with_most_factors) + " with: " + str(most_factors))

                if factors > 500:
                    print("Triangular Number found: " + str(TRI_NUM) + " with number of factors: " + str(factors))
                    return TRI_NUM
            
            print("Factors > 500 not found in triangular number set up to and including " + str(num))
            return "Factors > 500 not found in triangular number set up to and including " + str(num)

        solve(99999)

        # New largest num. of factors found: 2031120 with: 240
        # New largest num. of factors found: 2162160 with: 320
        # New largest num. of factors found: 17907120 with: 480
        # Above: 75638850
        # Triangular Number: 76576500 has number of factors: 576

    except Exception as ex:
        print('Exception: ' + str(ex))