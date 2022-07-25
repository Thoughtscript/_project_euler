# https://projecteuler.net/problem=31
# had to look up how people approached integer partitions - several algorithms
# cleanest implementation I found as follows
# from https://leetcode.com/submissions/detail/755940600/

if __name__ == '__main__':

    try:

        COIN_MAP = [1,2,5,10,20,50,100,200]

        # max total is max_n
        def prep_arr(max_n):
            arr = []
            for i in range(0, max_n + 1, 1):
                arr.append(0)

            # e.g. 10 - 10
            arr[0] = 1
            return arr

        def integer_partitions(max_n):
            arr = prep_arr(max_n)

            # general mathematical algorithm - integer partitions
            for i in range(0, len(COIN_MAP), 1):
                coin = COIN_MAP[i]

                for j in range(coin, max_n + 1, 1):
                    arr[j] = arr[j] + arr[j - coin]

            # print(arr)
            return arr[max_n]

        def find_combos(max_num):
            results = integer_partitions(max_num)
            print("Number of solutions found: " + str(results))
            return results
        
        find_combos(200) # 73682
            
    except Exception as ex:
        print('Exception: ' + str(ex))
