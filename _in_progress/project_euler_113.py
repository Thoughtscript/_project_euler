# https://projecteuler.net/problem=113

from decimal import *

if __name__ == '__main__':

    try:
        def increasing_or_decreasing(num):
            s = str(num)
            LEN = len(s)
            is_increasing = True
            is_decreasing = True

            for x in range(0, LEN, 1):
                if x < LEN - 1:
                    if int(s[x]) > int(s[x+1]) and is_increasing:
                        #print(str(num) + " is not an increasing number")
                        is_increasing = False
                        
                if x > 0:
                    if int(s[x-1]) < int(s[x]) and is_decreasing:
                        #print(str(num) + " is not a decreasing number")
                        is_decreasing = False

                if (not is_increasing and not is_decreasing):
                    break

            #if (is_increasing and not is_decreasing):
            #    print(str(num) + " is an increasing number")

            #if (not is_increasing and is_decreasing):
            #    print(str(num) + " is a decreasing number")

            return [is_increasing, is_decreasing]
            
        def is_bouncy(num):
            bools = increasing_or_decreasing(num)
            result = (bools[0] == False and bools[1] == False)
            #print(str(num) + " is bouncy: " + str(result))
            return result


        def solve(mx_num):
            not_bouncy_count = 0

            for x in range(1, mx_num, 1):
                if not is_bouncy(x):
                    not_bouncy_count += 1

            print("not_bouncy_count at " + str(mx_num) + " is: " + str(not_bouncy_count))
            ratio = Decimal(not_bouncy_count) / Decimal(x)
            print("Ratio: " + str(ratio))

        #solve(100000000) # not_bouncy_count at 100000000 is: 67986
        #solve(10000000) # not_bouncy_count at 10000000 is: 30816 
        #solve(1000000) # not_bouncy_count at 1000000 is: 12951
        #solve(100000) # not_bouncy_count at 1000000 is: 4953
        #solve(10000) # not_bouncy_count at 10000 is: 1674
        #solve(1000) # not_bouncy_count at 1000 is: 474

        '''
        10000000000   277032  Ratio: 0.0000277032
        100000000     67986   Ratio: 0.0006798600067986000679860006799    37,170      19,305
        10000000      30816   Ratio: 0.003081600308160030816003081600     17,865      9,393    
        1000000       12951   Ratio: 0.01295101295101295101295101295      8,472       5,193
        100000        4953    Ratio: 0.04953049530495304953049530495      3,279       2,079
        10000         1674    Ratio: 0.1674167416741674167416741674       1,200
        1000          474     Ratio: 0.4744744744744744744744744745       
        '''

        '''
        pow(10, 100)    >= 33 zeroes in decimal right of .
        '''

    except Exception as ex:
        print('Exception: ' + str(ex))