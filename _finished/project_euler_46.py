# https://projecteuler.net/problem=46

import primes_to_2mil as P

if __name__ == '__main__':

    try:

        def prime_map():
            primes = {}

            for x in range(0, len(P.primes), 1):
                primes[P.primes[x]] = True
            
            return primes
        
        PRIME_MAP = prime_map()

        def is_odd(num):
            return not num % 2 == 0
        
        def is_composite(num):
            return PRIME_MAP.get(num) is None
        
        def is_goldbach(num):
            # print("Testing for: " + str(num))
            for y in range(0, num, 1):
                current_prime = PRIME_MAP.get(y)

                if current_prime is None:
                    continue

                if y >= num:
                    return False
                
                print("Testing for current_prime: " + str(y))
                
                for z in range(0, num, 1):
                    val = y + 2 * (z * z)
                    # print("Testing sum of prime and twice a square: " + str(y) + " + 2 * " + str(z * z) + " = " + str(val))

                    if val == num:
                        return True
                    
                    if val > num:
                        break

            return False

        
        def solve():
            for x in range(5766, 999999, 1):
                if is_composite(x) and is_odd(x):
                    if not is_goldbach(x):
                        print("Smallest odd composite found for which Goldbach's Conjecture fails: " + str(x))
                        return
                    else:
                        print("Goldbach's Conjecture holds for odd composite number: " + str(x))

        solve() # 5777

    except Exception as ex:

        print('Exception: ' + str(ex))