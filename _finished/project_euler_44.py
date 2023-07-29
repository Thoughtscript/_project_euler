# https://projecteuler.net/problem=44

if __name__ == '__main__':

    try:

        pentagonal_map = {}
        pentagonal_arr = []
        num_pentagonals = 99999

        def makePentagonal(n):
            return n * (3 * n - 1) / 2
        
        def isPentagonal(n):
            check_pentagonal = pentagonal_map.get(n)
            if not check_pentagonal:
                return False
            return True
        
        def generatePentagonals():
            for x in range(1, num_pentagonals, 1):
                pentagonal = makePentagonal(x)
                pentagonal_map[pentagonal] = True
                pentagonal_arr.append(pentagonal)

            print("First " + str(num_pentagonals) + " pentagonals generated!")
            # print(pentagonal_arr)
            # print(pentagonal_map)
        
        def calcPair(x, y):
            S = x + y
            D = abs(x - y)

            if (isPentagonal(S) and isPentagonal(D)):
                 return D

            return False
        
        def solve():
            minimized_d = 99999999999999

            for x in range(0, num_pentagonals - 1, 1):
                for y in range(0, num_pentagonals - 1,1):
                    if x == y:
                        continue

                    X = pentagonal_arr[x]
                    Y = pentagonal_arr[y]
                    # print("Attempting X:" + str(X) + " Y:" + str(Y))
                    D = calcPair(X, Y)

                    if D is not False:
                        if minimized_d > D:
                            minimized_d = D
                            print("New minimized_D found: " + str(D) + " for X:" + str(X) + " Y:" + str(Y))
                            print("Verifying...")
                            if isPentagonal(X):
                                print(str(X) + " is Pentagonal")
                            else:
                                print(str(X) + " is wrong!")

                            if isPentagonal(X):
                                print(str(Y) + " is Pentagonal")
                            else:
                                print(str(Y) + " is wrong!")
                                return

                            if isPentagonal(X+Y):
                                print(str(X+Y) + " is Pentagonal")
                            else:
                                print(str(X+Y) + " is wrong!")

                            if isPentagonal(D):
                                print(str(D) + " is Pentagonal")
                            else:
                                print(str(D) + " is wrong!")

            if minimized_d == 99999999999999:
                print("No solution found for: " + str(num_pentagonals) + "-many pentagonals")
                return
            
            print("Solution found: " + str(minimized_d))
            return minimized_d     

        generatePentagonals()
        solve() # 5482660


    except Exception as ex:
        print('Exception: ' + str(ex))