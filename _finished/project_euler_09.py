# https://projecteuler.net/problem=9

if __name__ == '__main__':

    try:

        def solve():
            for a in range (0, 1001, 1):
                for b in range (0, 1001, 1):
                    for c in range (0, 1001, 1):
                        if (a + b + c == 1000 and a < b and b < c):
                            A = pow(a, 2) 
                            B = pow(b, 2)
                            C = pow(c, 2)
                            print("Triple: " + str(a) + " " + str(b) + " " + str(c))
                            if (A + B == C):
                                print("Triple found: " + str(a) + " " + str(b) + " " + str(c))
                                return [a, b, c]

            print("None found")
            return

        solve() #  200 375 425

    except Exception as ex:
        print('Exception: ' + str(ex))