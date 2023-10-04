# https://projecteuler.net/problem=206

import math

if __name__ == '__main__':

    try:
        # 1_2_3_4_5_6_7_8_9_0
        # Lower Bound: 1020304050607080900 ## So, 1010101010.101
        # Upper Bound: 1929394959697989990 ## So, 1389026623.1063
        
        # 378925613 vs 1000000000

        def check_num_string(num_str):
            if not num_str[18] == "0":
                return False
            if not num_str[0] == "1":
                return False
            if not num_str[2] == "2":
                return False            
            if not num_str[4] == "3":
                return False
            if not num_str[6] == "4":
                return False
            if not num_str[8] == "5":
                return False            
            if not num_str[10] == "6":
                return False
            if not num_str[12] == "7":
                return False
            if not num_str[14] == "8":
                return False            
            if not num_str[16] == "9":
                return False
            return True
               
        def solve():
            found = False
            for x in range(1010101010, 1389026624, 1):
                power_x = pow(x, 2)
                pow_num_str = str(power_x)
                sq_num_str = str(x)
                # print("Trying: " + sq_num_str + " is the square root of " + pow_num_str)
                if check_num_string(pow_num_str):
                    print("Solution found: " + sq_num_str + " is the square root of " + pow_num_str)
                    found = True
                    return

            if not found:
                print("Solution not found")

        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))