# https://projecteuler.net/problem=97

if __name__ == '__main__':

    try:

        def solve():
            num = 28433 * pow(2, 7830457) + 1
            str_num = str(num)
            L = len(str_num)
            if not L == 2357207: # Given in problem
                raise Exception("Incorrect answer!")
            
            last_ten = str_num[-10:]
            if not len(last_ten) == 10:
                raise Exception("Incorrect answer!")
            
            print(last_ten)
            return last_ten

        solve() # 8739992577

    except Exception as ex:

        print('Exception: ' + str(ex))