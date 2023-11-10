# https://projecteuler.net/problem=104

import sys

if __name__ == '__main__':

    def set_recursion_limit(n):
        sys.setrecursionlimit(n)
        
    def reset_recursion_limit():
        sys.setrecursionlimit(1000)

    try:

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

        def innerFib(arr, target, current):
            L = len(arr)
            N = arr[L - 2] + arr[L - 1]
            str_num = str(N)

            if len(str_num) >= 18:
                front = str_num[0:9]
                back = str_num[L-9:L]
                print(front)
                print(back)
                if is_pandigital(front) and is_pandigital(back):
                    print("Solution found: " + str_num)
                    return str_num

            arr[0] = arr[L - 1]
            arr[1] = N

            if current < target:
                current = current + 1
                return innerFib(arr, target, current)

        def fibonacci(target):
            MN = 1
            if target <= MN:
                print('Please enter a number greater than ' + str(MN))
            else:
                return innerFib([0,1], target, MN + 1)

        set_recursion_limit(9999999)

        fibonacci(99999)
                     
        reset_recursion_limit()

    except Exception as ex:
        print('Exception: ' + str(ex))