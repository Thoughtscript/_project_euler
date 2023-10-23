# https://projecteuler.net/problem=53

if __name__ == '__main__':

    try:
                
        def greater_than_million(str_num):
            return int(str_num) > 1000000
        
        def power_set(arrSet):
            arrSets = []

            for i in range(0, len(arrSet), 1):
                item = arrSet[i]
                origSets = arrSets

                for j in range(0, len(origSets), 1):
                    nSet = origSets[j] + [item]
                    arrSets.append(nSet)

                itemArr = [item]
                arrSets.append(itemArr)

            arrSets.append([])
            # print(arrSets)
            return arrSets
        
        #power_set([4,2,3]) # [[4], [4, 2], [2], [4, 3], [4, 2, 3], [2, 3], [3], []]
        #power_set([5, 1, 4, 2, 3]) 
        '''
        [
            [5], [5, 1], [1], [5, 4], [5, 1, 4], [1, 4], [4], [5, 2], [5, 1, 2], [1, 2], [5, 4, 2], 
            [5, 1, 4, 2], [1, 4, 2], [4, 2], [2], [5, 3], [5, 1, 3], [1, 3], [5, 4, 3], [5, 1, 4, 3],
             [1, 4, 3], [4, 3], [5, 2, 3], [5, 1, 2, 3], [1, 2, 3], [5, 4, 2, 3], [5, 1, 4, 2, 3], 
             [1, 4, 2, 3], [4, 2, 3], [2, 3], [3], []
        ]
        '''

        def select_n_from_r(arr, n):
            ps = power_set(arr)
            total = 0

            for x in range(0, len(ps), 1):
                if len(ps[x]) == n:
                    num_str = ""
                    for y in range(0, len(ps[x]), 1):
                        num_str += str(ps[x][y])
                    #print(num_str)
                    if (greater_than_million(num_str)):
                        print("Combinatoric Selection found: " + num_str)
                        total += 1

            #print(str(total))
            return total
                        
        #select_n_from_r([1,2,3,4,5], 3)
        
        def solve():
            total = 0
            for n in range(1, 101, 1):
                for r in range(1, n+1, 1):
                    arr = []
                    for x in range(1, n + 1, 1):
                        arr.append(x)
                    total += select_n_from_r(arr, r)

        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))