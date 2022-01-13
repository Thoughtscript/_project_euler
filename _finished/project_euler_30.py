# https://projecteuler.net/problem=30

if __name__ == '__main__':

    try:

        # Note sum of x power does not imply 
        # that the number in question be length x!!

        def check_string(num, exp):
            num_as_str = str(num)
            total = 0
            result = []
            for x in range(0, len(num_as_str), 1):
                val = pow(int(num_as_str[x]), exp)
                result.append(val)
                total = total + val

            if total == num:
                print("Sum of " + str(exp) + " powers found " + str(num))
                print(result)

            return [total == num, total]

        def solve(a, b, c):

            sum = 0

            for x in range(a, b + 1, 1):
                check = check_string(x, c)
                if check[0] == True:
                    if check[1] > 1:
                        sum = sum + check[1]

            print(sum)
            return sum

        solve(0, 1000000,5) # 443840
        solve(0, 1000000, 4) # 19316

    except Exception as ex:

        print('Exception: ' + str(ex))