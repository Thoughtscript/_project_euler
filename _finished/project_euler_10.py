# https://projecteuler.net/problem=10

if __name__ == '__main__':

    try:

        def make_prime(target, arr):
            for x in range(target + 1):
                if x == 1:
                    continue
                if x == 2:
                    continue
                if x == 3:
                    continue
                if x == 5:
                    continue
                if x == 7:
                    continue
                else:
                    flag = False
            
                    for y in arr:
                        if x % y == 0:
                            flag = True
                            break
     
                    if not flag:
                        arr.append(x)
   
            print(arr)
            return arr

        def sum_below(arr, mx):
            S = 0
            for x in arr:
                if x < mx:
                    S = S + x
            
            print("Sum of all values below " + str(mx) + " is " + str(S) + "\n")
            return S

        sum_below(make_prime(2000000, [2, 3, 5, 7]), 2000000)
        # sum_below(make_prime(35, [2, 3, 5, 7]), 2000000)
        # sum_below(make_prime(10, [2, 3, 5, 7]), 2000000)

    except Exception as ex:

        print('Exception: ' + str(ex))