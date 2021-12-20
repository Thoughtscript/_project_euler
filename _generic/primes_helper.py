# Generic Primes

if __name__ == '__main__':

    try:

        # Generate an 0-indexed array where:
        # sieve[i] = False indicates non-prime
        # sieve[i] = True indicates prime
        def sieve_of_eratosthenes(num):
            sieve = [0] * num
            sieve[0] = False
            # print(sieve)

            for x in range(2, num+1, 1):
                if sieve[x-1] is 0:
                    sieve[x-1] = True

                for y in range(x*2, num+1, x):
                    sieve[y-1] = False

                # print(sieve)

            print(sieve)
            return sieve

        def prime_factorization(num):
            # Offset num by one when accessing
            primes = sieve_of_eratosthenes(num)
            result = []
            rem = num

            while rem % 2 == 0:
                rem = rem / 2
                result.append(2)

            # Must be odd or not divisible by 2
            for x in range(3, num+1, 2):
                if (primes[x-1] == False):
                    continue

                while (rem % x == 0):
                    result.append(x)
                    rem = rem / x

                if rem == 1 or rem == 0:
                    break

            print(result)
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

            print(result)
            return result

        #sieve_of_eratosthenes(10)
        #sieve_of_eratosthenes(20)
        #sieve_of_eratosthenes(50)

        #prime_factorization(12)
        #prime_factorization(18)
        #prime_factorization(500)

        #number_of_divisors(24)
        #number_of_divisors(18)
        #number_of_divisors(10)
        #number_of_divisors(5)

    except Exception as ex:

        print('Exception: ' + str(ex))
