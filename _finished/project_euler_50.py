# https://projecteuler.net/problem=50
import primes_to_2mil as P

if __name__ == '__main__':

    try:
        PRIMES = P.primes
        PRIMES.sort()

        def prime_map():
            primes = {}
            for x in range(0, len(P.primes), 1):
                primes[P.primes[x]] = True
            return primes

        PRIME_MAP = prime_map()

        def solve():
            mx_num = 0
            max_547 = 0

            # 2, 3, 5, 7, 11, 13, ...
            # left-pointer
            for x in range(0, len(PRIMES), 1):
                sum = 0
                temp = []
                if PRIMES[x] >= 1000000:
                    break

                for y in range(x, len(PRIMES), 1):
                    NEXT_NUM = sum + PRIMES[y]
                    if NEXT_NUM >= 1000000:
                        break

                    temp.append(PRIMES[y])
                    sum = NEXT_NUM

                    IS_PRIME = not PRIME_MAP.get(NEXT_NUM) == None
                    if IS_PRIME:
                        # if len(temp) >= 6 and NEXT_NUM < 51:
                        #    print(str(NEXT_NUM))
                        #    print(temp)

                        # if len(temp) >= 21 and NEXT_NUM < 1000:
                        #    print(str(NEXT_NUM))
                        #    print(temp)

                        # print("Prime found: " + str(NEXT_NUM) + " with sequence length " + str(len(temp)))
                        if (mx_num < len(temp)):
                            mx_num = len(temp)
                            print("New max length found: " + str(len(temp)) + " for prime " + str(NEXT_NUM))
                                   
            return mx_num

        # Largest sequnce is 547
        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))