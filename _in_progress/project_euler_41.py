# https://projecteuler.net/problem=41

# This is equivalent to three+ mediums on LeetCode:
# https://leetcode.com/problems/permutations/ - Problem #46 Medium
# https://leetcode.com/problems/combinations/ - Problem #77 Medium
# https://leetcode.com/problems/count-primes/ - Problem #204 Medium

if __name__ == '__main__':

    try:

        LOW_PRIMES = [2,3,5,7,11,13,17]

        # This is Greedily coded to find prime numbers above 17.
        # E.g. - it won'y return 17 as prime!
        def find_primes(pandigital_numbers, largest):
            primes = []

            for x in range(0, len(pandigital_numbers), 1):
                orig_num = pandigital_numbers[x]
                num = pandigital_numbers[x]
                if num < largest:
                    print(str(num) + " skipped since it's lower than: " + str(largest))
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
                    print(str(orig_num) + " is not prime ")
                    continue

                not_prime = False

                for y in range(18, num, 1):
                    if num % y == 0:
                        not_prime = True
                        break
                
                if not_prime:
                    print(str(orig_num) + " is not prime ")
                    continue
                
                # This massively speeds things up!
                if num > largest:
                    largest = num
                    print(" ============================= ")
                    print("New Largest Prime Pandigital found: " + str(largest))

                primes.append(num)

            if len(primes) > 0:
                print(" ========= Primes that were larger than the current largest found: ========= ")
                primes.sort()
                print(primes)

            return primes

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
                    else:
                        print(key + " skipped since it's lower than: " + str(largest) + " during heaps")
                        
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
        # I solved problem 43 previously:
        # 1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289
        # are the only 6 Pandigital Numbers of length 10.
        # None of those are prime numbers, so the largest one is less than length 10.

        # It's at least as large as 9876413, Pandigital Number length 7.
        # It's at least as large as 98765431, Pandigital Number length 8.

        def map_to_arr(hm):
            result = []
            hmv = hm.values()

            for x in range(0, len(hmv), 1):
                result.append(int(hmv[x]))

            return result

        def solve():
            largest = 98765431
            for x in range(2, 10, 1):

                combos = combination(9, x)
                for y in range(0, len(combos), 1):

                    # Pass in largest to optimize!!!
                    heaps = permute(combos[y], largest)

                    # Pass in largest to optimize!!!
                    primes = find_primes(map_to_arr(heaps), largest)
                    if len(primes) > 0:
                        temp_largest = primes[len(primes) - 1]
                        if temp_largest > largest:
                            largest = temp_largest
                            print(" ============================= ")
                            print("New Largest Prime Pandigital found: " + str(largest))

            print(" ============================= ")
            print("Largest Prime Pandigital is: " + str(largest))
            return largest

        solve() # 76503241

    except Exception as ex:

        print('Exception: ' + str(ex))
