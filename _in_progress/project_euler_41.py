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
        def find_primes(pandigital_numbers):
            primes = []

            for x in range(0, len(pandigital_numbers), 1):
                num = pandigital_numbers[x]
                divisors = []

                for y in range(0, len(LOW_PRIMES), 1):
                    prime = LOW_PRIMES[y]

                    while (num % prime == 0):
                        divisors.append(prime)
                        num = num / prime

                # Either a number is Prime
                # Or it has 2 or more Prime Factors
                # So, if this is > 1, it's not Prime
                if len(divisors) > 1:
                    # print(divisors)
                    continue

                not_prime = False

                for y in range(18, num, 1):
                    if num % y == 0:
                        divisors.append(y)
                        num = num / y

                    if len(divisors) > 1:
                        not_prime = True
                        break
                
                if not_prime:
                    continue

                divisors.append(num)
                divisors.append(1)
                
                if len(divisors) == 2:
                    primes.append(num)

            print(" ========= Primes found: ========= ")
            print(primes)
            return primes

        # ----------------- #

        def make_key(arr):
            string_result = ""

            for x in range(0, len(arr), 1):
                string_result = string_result + str(arr[x])

            return string_result

        def permute(original_arr):
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
                    heaps_results[key] = int(key)
            
                for i in range(0, n, 1):
                    heaps_algorithm(n-1)
                    v = 0
                    if n % 2 == 0:
                        v = i
                    swap(n-1, v)

            heaps_algorithm(len(original_arr))
            # print(heaps_results)
            return heaps_results

        # permute([0])
        # permute([0,1])
        # permute([0,1,2])
        # permute([0,1,2,3])
        # permute([0,1,2,3,4])
        # permute([0,1,2,3,4,5])

        # ----------------- #

        # 1 2 3
        # 1 2 4
        # 1 3 4c

        # 1 2 3 4
        # 1 2 3 5
        # 1 2 4 5
        # 1 3 4 5
        # 2 3 4 5

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

        # combination(4, 4)
        # combination(3, 3)
        # combination(8, 3)
        # combination(5, 5)
        # combination(9, 5)

        # ----------------- #

        # The largest such n-digit Pandigital Number will be less than or equal to 9876543210.
        # I solved problem 43 previously:
        # 1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289
        # are the only 6 Pandigital Numbers of length 10.
        # None of those are prime numbers, so the largest one is less than length 10.

        def map_to_arr(hm):
            result = []
            hmv = hm.values()

            for x in range(0, len(hmv), 1):
                result.append(int(hmv[x]))

            return result

        def solve():
            # Can modify this row
            for x in range(2, 10, 1):
                combos = combination(9, x)
                for y in range(0, len(combos), 1):
                    heaps = permute(combos[y])
                    find_primes(map_to_arr(heaps))

        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))
