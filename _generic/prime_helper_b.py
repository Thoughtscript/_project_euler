# Generic Primes

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

        def make_and_print(num):
            PRIMES = map_num_to_arr(sieve_of_eratosthenes(num))

            print(PRIMES)
            file = open('primes_to_5_mil.py', 'w')
            file.write(str(PRIMES))
            file.close()

        make_and_print(5000000)

    except Exception as ex:

        print('Exception: ' + str(ex))
