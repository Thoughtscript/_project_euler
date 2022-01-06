# https://projecteuler.net/problem=41

# This is equivalent to two+ mediums on LeetCode:
# https://leetcode.com/problems/permutations/ - Problem #46 Medium
# https://leetcode.com/problems/count-primes/ - Problem #204 Medium

if __name__ == '__main__':

    try:

        LOW_PRIMES = [2,3,5,7,11,13,17]

        # This is Greedily coded to find prime numbers above 17.
        # E.g. - it won'y return 17 as prime!
        def find_primes(pandigital_numbers, largest):
            pandigital_numbers.sort(reverse=True)

            for x in range(0, len(pandigital_numbers), 1):
                orig_num = pandigital_numbers[x]
                num = pandigital_numbers[x]

                if num < largest:
                    # print(str(num) + " skipped since it's lower than: " + str(largest))
                    continue

                not_prime = False
                for y in range(0, len(LOW_PRIMES), 1):
                    prime = LOW_PRIMES[y]

                    # Either a number is Prime
                    # Or it has 2 or more Prime Factors
                    # So, if this is >= 1, it's not Prime
                    while (num % prime == 0):
                        not_prime = True
                        break

                if not_prime:
                    # print(str(orig_num) + " is not prime ")
                    continue

                not_prime = False

                for y in range(18, num / 2, 1):
                    if num % y == 0:
                        not_prime = True
                        break
                
                if not_prime:
                    # print(str(orig_num) + " is not prime ")
                    continue
                
                # This massively speeds things up!
                if num > largest:
                    largest = num
                    print(" ============================= ")
                    print("New Largest Prime Pandigital found: " + str(largest))

        # ----------------- #

        def make_key(arr):
            string_result = ""

            for x in range(0, len(arr), 1):
                string_result = string_result + str(arr[x])

            return string_result

        def permute(original_arr, largest):
            # print(original_arr)
            transfer_arr = original_arr
            heaps_results = {}

            def swap(end, begin):
                original = transfer_arr[begin]
                transfer_arr[begin] = transfer_arr[end]
                transfer_arr[end] = original

            def heaps_algorithm(n):
                if n == 1: 
                    key = make_key(transfer_arr)
                    if int(key) > largest:
                        heaps_results[key] = int(key)
                    # else:
                        # print(key + " skipped since it's lower than: " + str(largest) + " during heaps")
                    return
            
                for i in range(0, n, 1):
                    heaps_algorithm(n-1)
                    v = 0
                    if n % 2 == 0:
                        v = i
                    swap(n-1, v)

            heaps_algorithm(len(original_arr))
            return heaps_results

        # ----------------- #

        # Oops - save this probably useful later on - cannot include 0!
        # A Pandigital number of length n must include all numbers from 1 to n.

        def deep_copy(arr):
            new_arr = []

            for x in range(0, len(arr), 1):
                new_arr.append(arr[x])

            return new_arr

        def combination(n, k):
            ORIG_K = k
            result = []
            temp = []

            def inner(n, l, k):
                if len(temp) == ORIG_K:
                    new_arr = deep_copy(temp)
                    # print(new_arr)
                    result.append(new_arr)

                for x in range(l, n + 1, 1):
                    temp.append(x)
                    inner(n, x + 1, k - 1)

                    # Modified from:
                    # https://www.geeksforgeeks.org/make-combinations-size-k/?ref=gcse
                    # Super helpful!
                    temp.pop()

            inner(n, 0, k)
            print(" ========= Combinations: ========= ")
            print(result)
            return result

        # ----------------- #

        # The largest such n-digit Pandigital Number will be less than or equal to 9876543210.
        # A Pandigital number of length n must include ALL numbers from 1 to n!
        # The below solves for the looser scenario where a number of length n need only have no two digits repeated.

        # This is here to discharge the hashmap dict from memory rather 
        # than both passing the hashmap and calling the values() method.
        # It's unneeded in solve_b() but was a small memory optimization technique since I was hitting a billion+ numbers.
        def map_to_arr(hm):
            result = []
            hmv = hm.values()

            for x in range(0, len(hmv), 1):
                result.append(int(hmv[x]))

            return result

        def solve_a(set_largest, starting_length):
            largest = set_largest
            for x in range(starting_length, 11, 1):

                combos = combination(9, x)
                for y in range(0, len(combos), 1):

                    # Pass in largest to optimize!!!
                    heaps = permute(combos[y], largest)

                    # Pass in largest to optimize!!!
                    find_primes(map_to_arr(heaps), largest)

            print(" ============================= ")
            print("Largest Prime Pandigital is: " + str(largest))
            return largest


        # solve_a(0, 2)

        # ----------------- # 

        def solve_b():
            largest = 1234
            heaps = permute([2,1], largest)
            find_primes(map_to_arr(heaps), largest)

            heaps = permute([3,2,1], largest)
            find_primes(map_to_arr(heaps), largest)

            heaps = permute([4,3,2,1], largest)
            find_primes(map_to_arr(heaps), largest)

            heaps = permute([5,4,3,2,1], largest)
            find_primes(map_to_arr(heaps), largest)

            heaps = permute([6,5,4,3,2,1], largest)
            find_primes(map_to_arr(heaps), largest)

            heaps = permute([7,6,5,4,3,2,1], largest)
            find_primes(map_to_arr(heaps), largest)

            heaps = permute([8,7,6,5,4,3,2,1], largest)
            find_primes(map_to_arr(heaps), largest)

            heaps = permute([9,8,7,6,5,4,3,2,1], largest)
            find_primes(map_to_arr(heaps), largest)

        solve_b()

        # ----------------- # 

    except Exception as ex:

        print('Exception: ' + str(ex))
