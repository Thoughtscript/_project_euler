# https://projecteuler.net/problem=48

if __name__ == '__main__':

    try:

        def solve():
            sum = 0

            for x in range(1, 1001, 1):
                sum = sum + pow(x, x)
            
            num_str = str(sum)
            print(num_str)
            LEN = len(num_str)
            LAST_TEN = num_str[LEN-10:LEN]
            print(LAST_TEN)
            return LAST_TEN

        solve() # 9110846700

    except Exception as ex:

        print('Exception: ' + str(ex))