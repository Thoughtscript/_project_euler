# https://projecteuler.net/problem=57

if __name__ == '__main__':

    try:

        def solve():
            num = 3
            denom = 2
            result = 0

            last_num = 1
            last_denom = 1

            for x in range(0, 1001, 1):
                print("Trying: " + str(num) + "/" + str(denom))
                count_num_str = len(str(num))
                count_denom_str = len(str(denom))

                if (count_num_str > count_denom_str):
                    result += 1

                next_num = num
                next_denom = denom

                num = num * 2 + last_num
                denom = denom * 2 + last_denom

                last_num = next_num
                last_denom = next_denom

            print("Solution found: " + str(result))

        solve() # 153

    except Exception as ex:

        print('Exception: ' + str(ex))