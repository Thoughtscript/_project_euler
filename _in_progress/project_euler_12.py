# https://projecteuler.net/problem=12

import multiprocessing

if __name__ == '__main__':

    try:

        def generate(num):
            arr = []
            last = 0
            for x in range(1,num+1,1):
                y = x + last
                last = y
                if y % 2 == 0:
                    arr.append(y)

            print(arr)
            return arr

        # Will be even and above 69673110.
        # Probably ending in a 0.
        # Probably having 1-10 as divisors.
        # Need to understand the relationships of these first...

        def solve(tri_nums):
            for x in range(0, len(tri_nums),1):
                if tri_nums[x] < 69673110:
                    continue

                factors = []
                for y in range(1, tri_nums[x]+1, 1):
                    if tri_nums[x] % y == 0:
                        factors.append(y)
                print("Factors for: " + str(tri_nums[x]) + " are: " + str(factors))
                if len(factors) > 500:
                    print("Number found: " + str(tri_nums[x]) + " with factors: " + str(factors) + " length: " + str(len(factors)))
                    return tri_nums[x]
            
            return "None found"

        solve(generate(100000))

        # ----------------------------------------------

        def parallel_solve(num):
            if num < 58444266:
                print("Number below " + str(58444266))
                return
            
            factors = []
            for y in range(1, num+1, 1):
                if num % y == 0:
                    factors.append(y)
            print("Factors for: " + str(num) + " are: " + str(factors))

            if len(factors) > 500:
                print("Number found: " + str(num) + " with factors: " + str(factors) + " length: " + str(len(factors)))
                return num
            
        # Must to be above 100
        # pool = multiprocessing.Pool()
        # pool = multiprocessing.Pool(processes=4)
        # outputs = pool.map(parallel_solve, generate(100000))

        # ----------------------------------------------

    except Exception as ex:
        print('Exception: ' + str(ex))