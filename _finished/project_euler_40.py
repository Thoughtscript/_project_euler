# https://projecteuler.net/problem=40

if __name__ == '__main__':

    try:

        def solve():
            # Only generate the decimal integers after the point
            decimal_str = ''

            for x in range(1,1000000,1):
               decimal_str = decimal_str + str(x)

            # Offset by one
            A = decimal_str[1-1]
            B = decimal_str[10-1]
            C = decimal_str[100-1]
            D = decimal_str[1000-1]
            E = decimal_str[10000-1]
            F = decimal_str[100000-1]
            G = decimal_str[1000000-1]

            print(A)
            print(B)
            print(C)
            print(D)
            print(E)
            print(F)
            print(G)

            result = int(A) *int(B) * int(C) * int(D) * int(E) * int(F) * int(G)

            print("The answer is: " + str(result))
            return result

        solve() # 210

    except Exception as ex:

        print('Exception: ' + str(ex))