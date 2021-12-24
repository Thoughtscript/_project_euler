# https://projecteuler.net/problem=20

if __name__ == '__main__':

    try:

        def py_factor(num):
            total = 1

            for x in range(num, 0, -1):
                total = total * x
                # print(total)

            print(total)
            return total

        # py_factor(100) # 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

        def solve():
            num_str = str(py_factor(100))
            result = 0

            for x in range(0, len(num_str), 1):
                result = result + int(num_str[x])

            print(result)
            return result

        solve()
    
    except Exception as ex:

        print('Exception: ' + str(ex))