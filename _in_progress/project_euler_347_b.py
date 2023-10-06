# https://projecteuler.net/problem=347

if __name__ == '__main__':

    import time
    import math

    # This is a much much faster implementation.
    ## Iterates from 1 to mx_num
    ## Along the way performs faster prime factorization (instead of brute-force checking each prime number < curr_num)
    ## Uses a memoization largest hashmap auxiliary table to store the largest computed value in two-dimensions p x q 
    ## Still a bit slow over 100,000 but dramatically fewer operations.

    try:

        # mx_num = 100 # 2262
        # mx_num = 1000 # 193408
        # mx_num = 10000 # 16373230
        # mx_num = 100000 # 1414000891
        mx_num = 10000000
        
        def sieve_of_eratosthenes(num):
            sieve = [0] * num
            sieve[0] = False

            for x in range(2, num+1, 1):
                if sieve[x-1] is 0:
                    sieve[x-1] = True

                for y in range(x*2, num+1, x):
                    sieve[y-1] = False

            return sieve
        
        largest = {}
        primes = sieve_of_eratosthenes(mx_num)
        
        # Modified Prime Factorization
        def two_primes(num):
            result = {}
            rem = num

            while rem % 2 == 0:
                rem = rem / 2
                if result.get(2) is None:
                    result[2] = 1
                else:
                    result[2] += 1

            for x in range(3, num + 1, 2):
                # Small tweak here so no more than 3 primes are computed per curr_num
                if len(result.keys()) > 2:
                    break

                if (primes[x-1] == False):
                    continue

                while (rem % x == 0):
                    if result.get(x) is None:
                        result[x] = 1
                    else:
                        result[x] += 1

                    rem = rem / x

                if rem == 1 or rem == 0:
                    break

            return result    
        
        def sum_arr(arr):
            sum = 0

            for x in range(0, len(arr), 1):
                sum += arr[x]

            return sum
        
        # print(sum_arr([96, 100, 98, 88, 52, 68, 76, 92, 58, 62, 74, 82, 86, 94, 75, 63, 99, 39, 51, 57, 69, 87,93, 35, 55, 65, 85, 95, 77, 91])) # 2262
    
        def solve(mx):
            start = time.time()
            total_score = 0

            for x in range(1, mx + 1, 1):
                # print("Trying " + str(x))
                result = two_primes(x)
                keys = list(result.keys())
                if len(keys) == 2:
                    print("Number found: " + str(x) + " with " + str(keys))
                    keyA = keys[0]
                    keyB = keys[1]
                    if largest.get(keyA) is None:
                        largest[keyA] = {}
                    if largest.get(keyA).get(keyB) is None:
                        largest[keyA][keyB] = x
                    else:
                        largest[keyA][keyB] = max(largest[keyA][keyB], x)

            # Iterate through largest and sum value of each key.
            largest_keys = list(largest.keys())

            for x in range(0, len(largest_keys), 1):
                total_score += sum_arr(list((largest.get(largest_keys[x]).values())))          
            
            end = time.time()
            print("Total Score found: " +str(total_score) + " for " + str(mx) + " in " + str(end))

        solve(mx_num)

    except Exception as ex:

        print('Exception: ' + str(ex))