# https://projecteuler.net/problem=50

import primes_to_2mil as P

if __name__ == '__main__':

    try:

        PRIMES = P.primes
        PRIMES.sort()

        def solve(known_mx, known_mx_num):
            mx = known_mx
            mx_num = known_mx_num

            for x in range(0, len(PRIMES), 1):
                PRIME_NUM = PRIMES[x]

                if PRIME_NUM <= known_mx_num:
                    continue

                if PRIME_NUM >= 1000000:
                    break

                for y in range(0, x, 1):
                    sum = 0
                    temp = []
                    found = False

                    for z in range(y, x, 1):

                        if sum == PRIME_NUM:
                            # print("\nSum found for: " + str(PRIME_NUM) + " with length: " + str(len(temp)))
                            # print(temp)

                            # The first sequence found should be the largest!
                            found = True

                            if len(temp) > mx:
                                print("New largest sequence found with length: " + str(len(temp)) + " for: " + str(PRIME_NUM))
                                # print(temp)
                                mx = len(temp)
                                mx_num = PRIME_NUM
                                break
                        
                        if sum > PRIME_NUM:
                            break

                        sum = sum + PRIMES[z]
                        temp.append(PRIMES[z])

                    if found:
                        break

            print("Prime Number " + str(mx_num) + " can be written as the sum of " + str(mx) + " consecutive primes.")
            return mx_num

        # solve(0, 0)
        # solve(133,47711)
        # solve(155, 64613)

        # It is not true that the larger the prime the larger the sequence!
        # My guess is that somewhere in the sequence, the number actually starts decreasing?
        # Checking from the end to the beginning (the primes closest to 1000000) yields surprisingly smaller sequences.

        # I got 29 for 999983
        # I got 27 for 999979

        solve(183, 92951)

    except Exception as ex:

        print('Exception: ' + str(ex))