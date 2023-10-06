# https://projecteuler.net/problem=58

if __name__ == '__main__':

    import primes_to_5_mil as PRIMES

    try:

        def init(x):
            matrix = [[]] * x

            for y in range(0, x, 1):
                row = [0] * x
                matrix[y] = row

            return matrix    
    
        def checkRight(matrix, r, c, n):
            if c+1 >= n:
                return False
            nxt = matrix[r][c+1]
            return nxt == 0
    
        def checkLeft(matrix, r, c, n):
            if c-1 < 0:
                return False
            nxt = matrix[r][c-1];
            return nxt == 0
    
        def checkDown(matrix, r, c, n):
            if r+1 >= n:
                return False
            nxt = matrix[r+1][c]
            return nxt == 0
    
        def checkUp(matrix, r, c, n):
            if r-1 < 0:
                return False
            nxt = matrix[r-1][c]
            return nxt == 0 
        
        def makeSpiral(n):
            matrix = init(n)
            counter = n * n
            row = n - 1
            col = n - 1
            direction = 2

            while counter > 0:
                while direction == 0 and counter > 0:
                    matrix[row][col] = counter
                    counter -= 1
                    col += 1
                    if not checkRight(matrix, row, col, n):
                        direction += 1
            
                while direction == 1 and counter > 0:
                    matrix[row][col] = counter;
                    counter -= 1
                    row += 1
                    if not checkDown(matrix, row, col, n):
                        direction += 1
            
                while direction == 2 and counter > 0:
                    matrix[row][col] = counter
                    counter -= 1
                    col -= 1
                    if not checkLeft(matrix, row, col, n):
                        direction += 1
            
            
                while direction == 3 and counter > 0:
                    matrix[row][col] = counter
                    counter -= 1
                    row -= 1
                    if not checkUp(matrix, row, col, n):
                        direction = 0
        
            print(matrix)
            return matrix
        
        # makeSpiral(9) # [[65, 64, 63, 62, 61, 60, 59, 58, 57], [66, 37, 36, 35, 34, 33, 32, 31, 56], [67, 38, 17, 16, 15, 14, 13, 30, 55], [68, 39, 18, 5, 4, 3, 12, 29, 54], [69, 40, 19, 6, 1, 2, 11, 28, 53], [70, 41, 20, 7, 8, 9, 10, 27, 52], [71, 42, 21, 22, 23, 24, 25, 26, 51], [72, 43, 44, 45, 46, 47, 48, 49, 50], [73, 74, 75, 76, 77, 78, 79, 80, 81]]
        # makeSpiral(7) # [[37, 36, 35, 34, 33, 32, 31], [38, 17, 16, 15, 14, 13, 30], [39, 18, 5, 4, 3, 12, 29], [40, 19, 6, 1, 2, 11, 28], [41, 20, 7, 8, 9, 10, 27], [42, 21, 22, 23, 24, 25, 26], [43, 44, 45, 46, 47, 48, 49]]
        # makeSpiral(5) # [[17, 16, 15, 14, 13], [18, 5, 4, 3, 12], [19, 6, 1, 2, 11], [20, 7, 8, 9, 10], [21, 22, 23, 24, 25]]

        def prime_map():
            primes = {}

            for x in range(0, len(PRIMES.primes), 1):
                primes[PRIMES.primes[x]] = True
            
            return primes

        PRIME_MAP = prime_map()

        def calcDiags(matrix):
            n = len(matrix)
            count_primes = 0
            count_non_primes = 0

            for x in range(0, n, 1):
                num = matrix[x][x]
                if PRIME_MAP.get(num) is None:
                    count_non_primes += 1
                else:
                    count_primes += 1
            
            for x in range(0, n, 1):
                c = n - x - 1
                r = x

                num = matrix[r][c]
                if PRIME_MAP.get(num) is None:
                    count_non_primes += 1
                else:
                    count_primes += 1

            print("count_primes " + str(count_primes) + " count_non_primes " + str(count_non_primes - 1))
            return count_primes / (count_primes + count_non_primes - 1)
        
        def solve():
            for x in range (2493, 3000, 2): # 1781, 3050 # 2997 -> 3047
                percentile = calcDiags(makeSpiral(x))
                print("Attempt: " + str(x) + " at " + str(percentile))
                if percentile < .1:
                    print("Solution found: " + str(x) + " at " + str(percentile))
                    break

        #solve() 
        # print(calcDiags(makeSpiral(7))) # count_primes 8 count_non_primes 5
                                          # 0.6153846153846154

        # print(calcDiags(makeSpiral(3047))) <- Puzzled since this seems correct

    except Exception as ex:

        print('Exception: ' + str(ex))