# https://projecteuler.net/problem=31

if __name__ == '__main__':

    try:

        COIN_MAP = [1,2,4,10,20,50,100,200]

        # Minimum case is 1.
        # Maximum case is 200.
        # Backtracking?

        def append_return(arr, val):
            temp = arr
            temp.append(val)
            return temp

        # Create new deep copy
        def concat(a, b):
            result = []

            for x in range(0, len(a), 1):
                result.append(a[x])

            for y in range(0, len(b), 1):
                result.append(b[y])

            return result
    

        # TBD Backtracking
        def try_next(current, temp_arr, total):
            # print(str(temp_arr))
            new_arr = concat(temp_arr, [])

            if len(temp_arr) > 200:
                return False

            if current > 200:
                return False

            if current == 200:
                return True

            for x in range(0, len(COIN_MAP), 1):
                coin = COIN_MAP[x]
                next_amount = current + coin
                check = try_next(next_amount, append_return(new_arr, coin), total)
                
                if check == True:
                    print("\nCombination found:")
                    print(temp_arr)
                    total = total + 1

            return total

        def solve():
            total = 0

            for x in range(0, len(COIN_MAP), 1):
                coin = COIN_MAP[x]
                total = total + try_next(coin, [coin], 0)

            print("Total ways found: " + str(total))

        solve()
            
    except Exception as ex:

        print('Exception: ' + str(ex))