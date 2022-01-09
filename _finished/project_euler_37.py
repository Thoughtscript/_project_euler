# https://projecteuler.net/problem=37

import primes_to_2mil as PRIMES

if __name__ == "__main__":

    try:

        def prime_map():
            primes = {}

            for x in range(0, len(PRIMES.primes), 1):
                primes[PRIMES.primes[x]] = True
            
            # print(primes)
            return primes

        PRIME_MAP = prime_map()

        def is_prime(num_str):
            VAL = PRIME_MAP.get(int(num_str))
            result = not VAL is None
            # print(num_str + " is prime: " + str(result))
            return result

        # is_prime("101010")
        # is_prime("79")
        # is_prime("7")
        # is_prime("1382399")
            
        # A left to right and right to left truncatable prime:
        # Must start with 2, 3, 5, or 7
        # End with 2, 3, 5, or 7
        # Those are the only single digit primes.

        def is_truncatable(num_str):
            if not (num_str[0] == "2" or num_str[0] == "3" or num_str[0] == "5" or num_str[0] == "7"):
                # print(num_str + " is not a truncatable prime")
                return False

            LEN = len(num_str)
            LAST = num_str[LEN - 1]

            if not (LAST == "2" or LAST == "3" or LAST == "5" or LAST == "7"):
                # print(num_str + " is not a truncatable prime")
                return False

            for x in range(0, LEN, 1):
                # Left to Right
                temp_fwd = num_str[0+x:LEN]
                # Right to Left no reversal!
                temp_bwd = num_str[0:LEN-x]

                # print(temp_fwd)
                # print(temp_bwd)

                if is_prime(temp_fwd) and is_prime(temp_bwd):
                    continue
                else:
                    # print(num_str + " is not a truncatable prime")
                    return False

            # print(num_str + " is a truncatable prime")
            return True

        # is_truncatable("3797")
        # is_truncatable("20000")
        # is_truncatable("132321")
        # is_truncatable("13883")
        # is_truncatable("293213")
        # is_truncatable("5000")

        def solve():
            result = []
            for x in range(0, 2000000, 1):
                if is_truncatable(str(x)):
                    print("Is truncatable prime found: " + str(x))
                    result.append(x)
            
            print("Found " + str(len(result)) + " truncatable primes")
            print(result)

            sum = 0

            for x in range(0, len(result), 1):
                # Need to exclude 2,3,5,7 from answer
                if result[x] == 2 or result[x] == 3 or result[x] == 5 or result[x] == 7:
                    continue
                else:
                    sum = sum + int(result[x])

            print("Sum found: " + str(sum))
            return sum

        solve() # 748317

    except Exception as ex:

        print("Exception: " + str(ex))