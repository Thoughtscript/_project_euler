# https://projecteuler.net/problem=88

# k number of multiples and numbers being added

# n the smallest such number for some k such that
# the product and sums are equivalent and share
# the same operand digits

import copy

if __name__ == '__main__':

    try:

        def sum_arr(arr):
            sum = 0
            for i in range(0, len(arr), 1):
                sum += arr[i]
            return sum

        def mult_arr(arr):
            prod = 1
            for i in range(0, len(arr), 1):
                prod = prod * arr[i]
            return prod

        def find_min_prod_sum(k, divisors, current_num):
            results = []

            for j in range(0, len(divisors), 1):
                results.append([divisors[j]])

            j = 1
            while (j < k):
                temp = []
                for i in range(0, len(results), 1):
                    for l in range(0, len(divisors), 1):
                        inner_temp = copy.deepcopy(results[i]) 
                        inner_temp.append(divisors[l])

                        # arrays must be equal at k and any k-1
                        if sum_arr(inner_temp) == mult_arr(inner_temp):
                            temp.append(inner_temp)

                results = copy.deepcopy(temp)
                j += 1

            for j in range(0, len(results), 1):
                if sum_arr(results[j]) == mult_arr(results[j]):
                    print(str(results[j]) + " found as solution for " + str(current_num))
                    return True

            return False

        def divisors(n):
            divs = []
            for i in range(1, n+1,  1):
                if n % i == 0:
                    divs.append(i)

            #print("Divisors found for " + str(n) + " " + str(divs))
            return divs

        def solve(k):
            results = []

            # increment numbers
            # can never be 1 or 2
            # and will always grow
            current_num = 3

            # number of operands
            for i in range(2, k+1, 1):
                print("Starting solutions for k=" + str(i))
                while True:
                    # find divisors
                    divs = divisors(current_num)
                    if find_min_prod_sum(i, divs, current_num):
                        print("Minimal product-sum found for k=" + str(i) + " num is " + str(current_num))
                        results.append(current_num)
                        break
                    
                    current_num += 1

            print(results)
            results_sum = sum_arr(results)
            print(results_sum)
            return results_sum

        solve(9) # 4 6 6 8 8 12 12
        # deduplicated up to 2 <= k <= 12 is  {4, 6, 8, 12, 15, 16}

    except Exception as ex:

        print('Exception: ' + str(ex))