# https://projecteuler.net/problem=41

if __name__ == '__main__':

    try:

        LOW_PRIMES = [2,3,5,7,11,13,17]

        def find_primes(pandigital_numbers):
            for x in range(0, len(pandigital_numbers), 1):
                num = pandigital_numbers[x]
                divisors = []

                for y in range(0, len(LOW_PRIMES), 1):
                    prime = LOW_PRIMES[y]

                    while (num % prime == 0):
                        divisors.append(prime)
                        num = num / prime

                for y in range(18, num, 1):
                    if num % y == 0:
                        divisors.append(y)
                        num = num / y

                divisors.append(num)
                print(divisors)

        # ----------------- #

        def deep_copy(arr):
            string_result = ""

            for x in range(0, len(arr), 1):
                string_result = string_result + str(arr[x])

            return string_result

        def permute(original_arr):
            transfer_arr = original_arr
            heaps_results = {}

            def swap(end, begin):
                original = transfer_arr[begin]
                transfer_arr[begin] = transfer_arr[end]
                transfer_arr[end] = original

            def heaps_algorithm(n):
                if n == 1: 
                    key = deep_copy(transfer_arr)
                    heaps_results[key] = int(key)
            
                for i in range(0, n, 1):
                    heaps_algorithm(n-1)
                    v = 0
                    if n % 2 == 0:
                        v = i
                    swap(n-1, v)

            heaps_algorithm(len(original_arr))
            print(heaps_results)
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
        # 1 3 4

        # 1 2 3 4
        # 1 2 3 5
        # 1 2 4 5
        # 1 3 4 5
        # 2 3 4 5

        def combination(arr, sz):
            LEN = len(arr)

            if sz > LEN:
                return 

            if sz == LEN:
                print(arr)
                return arr

            results = []

            for x in range(0, LEN, 1):
                combo = [arr[x]]
                
                for y in range(x + 1, x + sz, 1):
                    if y >= LEN:
                        break

                    combo.append(arr[y])

                results.append(combo)

            print(results)
            return results

        DIGITS = [1,2,3,4,5]
        # combination(DIGITS, 4)

        def solve():

            # I solved problem 43 previously:
            # [1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289] 
            # are the only 6 Pandigital Numbers of length 10.

            # The largest such n-digit Pandigital Number will be less than or equal to 9876543210.
            # There are none of length 10.
            for x in range(2, 10, 1):
                combination = combination(DIGITS, x)
                heaps = permute(combination)
                print(find_primes(heaps))

        # solve()

    except Exception as ex:

        print('Exception: ' + str(ex))
