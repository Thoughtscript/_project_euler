# https://projecteuler.net/problem=36

import math

if __name__ == "__main__":

    try:

        def is_palindrome(num_str):
            LEN = len(num_str)
            HALF = int(math.floor(len(num_str) / 2))

            for x in range(0, HALF, 1):
                if num_str[x] == num_str[LEN - 1 - x]:
                   continue
                else:
                    #print(num_str + " is not a palindrome")
                    return False
            
            #print(num_str + " is a palindrome")
            return True

        def to_binary(num):
            return format(num, 'b')

        # print(to_binary(585))

        def solve():

            result = []

            for x in range(0, 1000000, 1):
                num_str = str(x)
                A = is_palindrome(num_str)
                binary = to_binary(x)
                B = is_palindrome(binary)

                if A and B:
                    print("Double-base palindrome found: " + num_str)
                    result.append(x)

            print(result)

            sum = 0

            for x in range(0, len(result), 1):
                sum = sum + int(result[x])

            print("Sum found: " + str(sum))
            return sum
       
        solve()
      
    except Exception as ex:

        print("Exception: " + str(ex))