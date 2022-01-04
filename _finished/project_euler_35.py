# https://projecteuler.net/problem=35

import primes_to_2mil as P

if __name__ == '__main__':

    try:

        # Convert to hashmap for optimization O(1) search
        # Below 1000000
        def prime_map():
            primes = {}

            for x in range(0, len(P.primes), 1):
                primes[P.primes[x]] = True

                if P.primes[x] > 1000000:
                    break
            
            # print(primes)
            return primes

        PRIME_MAP = prime_map()


        def is_circular(num):
            rotation = str(num)
            LEN = len(rotation)
            count = 0

            while count < LEN:
                # print(rotation)
                check = PRIME_MAP.get(int(rotation))

                if check is None:
                    return False

                count = count + 1
                rotation = rotation[1:LEN] + rotation[0]

            print(str(num) + " is circular")
            return True


        def solve():
            count = 0

            for x in range(0, 1000000, 1):
                if is_circular(x):
                    count = count + 1

            print(str(count) + " circular numbers found!")
            return count


        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))