# https://projecteuler.net/problem=55
import math

if __name__ == '__main__':

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

        #is_palindrome("111111")
        #is_palindrome("111112")
        #is_palindrome("141112")
        #is_palindrome("2")

        def reverse_num_str(num_str):
            result = ''
            for x in range(len(num_str) - 1, -1, -1):
                result = result + num_str[x]

            #print(result + " is the reversed string of: " + num_str)
            return result

        #reverse_num_str('1234')
        #reverse_num_str('7777')
        #reverse_num_str('000000000000001')

        # ------------- #

        # Lychrel numbers do not form palindromes when added to their reversed number.
        def solve(mx, iter):
            result = 0
            num_str = '0'
            reversed_num_str = '0'
            val = 0
            val_str = '0'

            for x in range(0, 10000, 1):
                orig_num = str(x)
                found = False
                for y in range(0, iter, 1):
                    if y == 0:
                        num_str = orig_num
                    else:
                        num_str = val_str
                        
                    reversed_num_str = reverse_num_str(num_str)
                    val = int(num_str) + int(reversed_num_str)
                    val_str = str(val)
                    if is_palindrome(val_str):
                        found = True
                        # print("Paldinrome found: " + orig_num + " on iteration: " + str(y) + " it was: " + str(val_str))
                        break

                if not found:
                    print("Lychrel number found: " + orig_num)
                    result = result + 1


            
            print("There are " + str(result) + " Lychrel numbers below " + str(mx))
            return result

        solve(10000, 50) # 249


    except Exception as ex:

        print('Exception: ' + str(ex))