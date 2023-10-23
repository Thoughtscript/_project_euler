# https://projecteuler.net/problem=243

from decimal import *

if __name__ == '__main__':

    try:

        def is_resilient_proper_fraction(n, d):
            mx = max(n, d)

            for x in range(2, mx, 1):
                if n % x == 0 and d % x == 0:
                    return False

            return True

        def solve(mx_num):
            target = Decimal(15499) / Decimal(94744)

            for d in range(2, mx_num+1, 1):
                print("Trying d: " + str(d))
                resilient = 0
                non_resilient = 0

                for n in range(1, d, 1):
                    if is_resilient_proper_fraction(n, d):
                        resilient += 1
                    else:
                        non_resilient += 1
                
                ratio = Decimal(resilient) / Decimal(resilient + non_resilient)
                print("Current ratio: " + str(ratio) + " with target: " + str(target))
                    
                if ratio < target:
                    print("Solution found for d: " + str(d))
                    return d
                    
            print("No solution found!")

        solve(9999999)
                         
    except Exception as ex:

        print('Exception: ' + str(ex))