# https://projecteuler.net/problem=12

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

            # print(sieve)
            return sieve

         # Offset num by one when accessing
        
        def prime_factorization(num, primes):
            result = []
            rem = num

            while rem % 2 == 0:
                rem = rem / 2
                result.append(2)

            # Must be odd or not divisible by 2 once it reaches here
            for x in range(3, num+1, 2):
                if (primes[x-1] == False):
                    continue

                while (rem % x == 0):
                    result.append(x)
                    rem = rem / x

                if rem == 1 or rem == 0:
                    break

            # print(result)
            return result

        def number_of_divisors(num, primes):
            prime_factors = prime_factorization(num, primes)
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
            primes = sieve_of_eratosthenes(triangulars[len(triangulars)-1])

            for x in range(0, len(triangulars),1):
                factors = number_of_divisors(triangulars[x], primes)
                print("Triangular Number: " + str(triangulars[x]) + " has number of factors: " + str(factors))

                if factors > 500:
                    print("Triangular Number found: " + str(triangulars[x]) + " with number of factors: " + str(factors))
                    return triangulars[x]
            
            print("Factors > 500 not found in triangular number set up to and including " + str(num))
            return "Factors > 500 not found in triangular number set up to and including " + str(num)

        # This is the upper limit here.
        # num = 10000000
        # primes = sieve_of_eratosthenes(num)
        # print(number_of_divisors(num, primes))
        # print(prime_factorization(num, primes))

        solve(99999)

    except Exception as ex:
        print('Exception: ' + str(ex))