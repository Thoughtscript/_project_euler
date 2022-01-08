# https://projecteuler.net/problem=32

if __name__ == '__main__':

    try:

        # ----------------- #

        def map_to_arr(hm):
            result = []
            hmv = hm.values()

            for x in range(0, len(hmv), 1):
                result.append(int(hmv[x]))

            # print(result)
            return result

        def make_key(arr):
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
                    key = make_key(transfer_arr)
                    heaps_results[key] = int(key)
                    return
            
                for i in range(0, n, 1):
                    heaps_algorithm(n-1)
                    v = 0
                    if n % 2 == 0:
                        v = i
                    swap(n-1, v)

            heaps_algorithm(len(original_arr))
            # print(heaps_results)
            return heaps_results

        # ----------------- #

        def make_arr_key(a, b, c):
            return make_key(a) + "-" + make_key(b) + "-" + make_key(c)

        # 1,1,7
        # 2,1,6
        # 7,1,1
        # 1,7,1
        def create_expressions(num):
            NUM_STR = str(num)
            # print("Creating expressions for " + NUM_STR)
            MIN = 1
            MAX = len(NUM_STR) - 1 - 1 + MIN
            expressions = []
            # Deduplicate
            hm={}

            # Iterate through ending indicies
            # This was tricky!
            for x in range(MIN, MAX, 1):
                multiplicand = NUM_STR[0:x]

                for y in range(MIN, MAX, 1):
                    multiplier = NUM_STR[x:x+y]

                    for z in range(MIN, MAX, 1):
                        product = NUM_STR[x+y:x+y+z]

                        if len(multiplicand) + len(multiplier) + len(product) == len(NUM_STR):
                            if len(multiplicand) > 0 and len(multiplier) > 0 and len(product) > 0:
                                if int(multiplicand) * int(multiplier) == int(product):
                                    KEY = make_arr_key(multiplicand, multiplier, product)
                                    # print(KEY)

                                    VAL = hm.get(KEY)
                                    if VAL is None:
                                        hm[KEY] = [multiplicand, multiplier, product]
                                        expressions.append([multiplicand, multiplier, product])

            # print(expressions)
            return expressions

        def is_pandigital(num):
            LEN = len(num)

            hm = {}
            for x in range(0, LEN, 1):
                N = int(num[x])

                if not (N >= 1 and N <= LEN):
                    # print(False)
                    return False

                V = hm.get(N)
                if V is None:
                    hm[N] = N
                else:
                    # print(False)
                    return False

            # print(True)
            return True

        #is_pandigital('456712389')
        #is_pandigital('123456789')
        #is_pandigital('123456781')
        #is_pandigital('0')
        #is_pandigital('1000')

        def check(exps, hm):
            product = int(exps[2])
            result = int(exps[0]) * int(exps[1]) == product
            if result:
                VAL = hm.get(product)
                if VAL is None:
                    hm[product] = [exps[0], exps[1], exps[2]]
                    return True

            return False

        def solve():
            DATA = [
                [1],
                [2,1],
                [3,2,1],
                [4,3,2,1],
                [5,4,3,2,1],
                [6,5,4,3,2,1],
                [7,6,5,4,3,2,1],
                [8,7,6,5,4,3,2,1],
                [9,8,7,6,5,4,3,2,1]
            ]

            hm={}

            result = 0

            for x in range(0, len(DATA), 1):
                heaps = map_to_arr(permute(DATA[x]))
                for y in range(0, len(heaps), 1):
                    exp = create_expressions(heaps[y])
                    
                    for z in range(0, len(exp), 1):
                        C = check(exp[z], hm)
                        if C:
                            print("New Pandigital Product found: " + exp[z][2])
                            result = result + int(exp[z][2])

            print(hm)

            VALS = hm.values()

            for x in range(0, len(VALS), 1):
                num_str = VALS[x][0] + VALS[x][1] + VALS[x][2]
                C = is_pandigital(num_str)
                if C == False:
                    print("Invalid values found! " + num_str)
                    print(VALS[x])
                    raise Exception

            print("Sum of Unique Pandigital Products found: " + str(result))
            return result

        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))