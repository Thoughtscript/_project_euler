# https://projecteuler.net/problem=808

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

        PRIMES = map_num_to_arr(sieve_of_eratosthenes(80000000))

        def prime_map():
            primes = {}

            for x in range(0, len(PRIMES), 1):
                primes[PRIMES[x]] = True
            
            return primes

        PRIME_MAP = prime_map()

        def check_prime(num_str):
            num = int(num_str)

            SQ_RT = pow(num, 1/2)

            if PRIME_MAP.get(SQ_RT) is None:
                return False

            return True

        # If not palindrome forward, not palindrome backwards.
        def is_palindrome(num_str):
            LEN = len(num_str)
            HALF = int(math.floor(len(num_str) / 2))

            if LEN == 1:
                return True

            for x in range(0, HALF, 1):
                if num_str[x] == num_str[LEN - 1 - x]:
                    continue

                else:
                    return False
            
            return True

        # No guarantee that reversed num is also in lowest/first 50 for probably 10+ such.
        def reverse_num_str(num_str):
            result = ''

            for x in range(len(num_str) - 1, -1, -1):
                result = result + num_str[x]

            # print(result + " is the reversed string of: " + num_str)
            return result

        def is_reversible_prime_square(num_str):
            if not is_palindrome(num_str):
 
                reversed = reverse_num_str(num_str)
                if not check_prime(int(reversed)):
                    return False
                
                return int(num_str)
            return False

        def solve():
            count = 0
            total = 0

            for x in range(0, len(PRIMES), 1):
                if (count == 50):
                    break

                squared = int(math.pow(PRIMES[x], 2))

                to_sum = is_reversible_prime_square(str(squared))

                if to_sum:
                    print(str(to_sum) + " reversible prime square found!")
                    count += 1
                    total += to_sum

            print(str(count) + " reversible prime squares found! " + str(total) + " resulting sum")
            return total

        solve() # 3807504276997394

    except Exception as ex:

        print('Exception: ' + str(ex))
