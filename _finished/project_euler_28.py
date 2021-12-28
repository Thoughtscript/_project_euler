# https://projecteuler.net/problem=28

if __name__ == '__main__':

    try:

        # Max num: 1002001
        # 500 right, 500 left
        # 500 top, 500 bootom
        # 500 diag each way

        #   111  112  113  114  115  116  117  118  119  120  121
        #   110  073  074  075  076  077  078  079  080  081  082
        #   109  072  043  044  045  046  047  048  049  050  083
        #   108  071  042  021  022  023  024  025  026  051  084
        #   107  070  041  020  007  008  009  010  027  052  085
        #   106  069  040  019  006  001  002  011  028  053  086
        #   105  068  039  018  005  004  003  012  029  054  087
        #   104  067  038  017  016  015  014  013  030  055  088
        #   103  066  037  036  035  034  033  032  031  056  089
        #   102  065  064  063  062  061  060  059  058  057  090
        #   101  100  099  098  097  096  095  094  093  092  091

        # 1 9 25 49 81
        # -> 3^2 5^2 7^2 9^2

        # 1 3 13 31 57
        # -> 2 10 18 26
        # ->  8  8  8 
        # Second order derivative remains constant 8

        # 1 5 17 37 65
        # -> 4 12 20 28
        # ->  8  8  8
        # Second order derivative remains constant 8

        # 1 7 21 43 73
        # -> 6 14 22 30
        # ->  8  8  8
        # Second order derivative remains constant 8

        def sum(arr):
            total = 0

            for x in range(0, len(arr), 1):
                total = total + arr[x]

            return total

        def solve(num):
            half = (num - 1) / 2
            
            # Upper right
            # 9 25 49 81
            y = 1
            val = 1
            upper_right = []
            for x in range(0, half, 1):
                y = y + 2
                val = pow(y, 2)
                upper_right.append(val)

            if not upper_right[len(upper_right) - 1] == 1002001:
                print("Last val should be 1002001")
                raise Exception("Last val should be 1002001")
                return

            # Lower right
            # 1 3 13 31 57
            # -> 2 10 18 26
            # ->  8  8  8 
            y = 10
            z = 8
            val = 1
            lower_right = []
            for x in range(0, half, 1):
                if x == 0:
                    val = 3
                else:
                    val = val + y
                    y = y + z

                lower_right.append(val)
                
            # Upper left
            # 1 7 21 43 73
            # -> 6 14 22 30
            # ->  8  8  8
            y = 14
            z = 8
            val = 7
            upper_left = []
            for x in range(0, half, 1):
                if x == 0:
                    val = 7
                else:
                    val = val + y
                    y = y + z

                upper_left.append(val)

            # Lower left
            # 1 5 17 37 65
            # -> 4 12 20 28
            # ->  8  8  8
            y = 12
            z = 8
            val = 1
            lower_left = []
            for x in range(0, half, 1):
                if x == 0:
                    val = 5
                else:
                    val = val + y
                    y = y + z

                lower_left.append(val)

            print(upper_right)
            print(lower_right)
            print(lower_left)
            print(upper_left)

            result = 1 + sum(upper_right) + sum(lower_right) + sum(lower_left) + sum(upper_left)
            print(result)
            return result

        solve(1001)

    except Exception as ex:

        print('Exception: ' + str(ex))