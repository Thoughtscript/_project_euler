# https://projecteuler.net/problem=725

import project_euler_725_STR_HM
import project_euler_725_SUM_HM

if __name__ == '__main__':

    try:
        def sum_digit_str(num_str):
            total = 0
            for x in range(0, len(num_str), 1):
                total += int(num_str[x])
            return total

        def generate_all_n_digit_strings(n, str_map):
            if n < 1:
                raise Exception
            
            if n == 1:
                # cannot start with 0
                str_map[1] = ["1","2","3","4","5","6","7","8","9"]
                return str_map.get(1)
            
            last_arr = str_map.get(n-1)
            counter = n-1

            while counter < n:
                temp = []
                for x in range(0, len(last_arr), 1):
                    curr_str = last_arr[x]

                    for y in range(0, 10, 1):
                        next_str = curr_str
                        next_str += str(y)
                        if not sum_digit_str(next_str) > 18:
                            temp.append(next_str)
                        else:
                            break
                    
                last_arr = temp
                counter += 1

            str_map[n] = last_arr
            return last_arr
        
        def is_ds_num(num_str):
            total = sum_digit_str(num_str)
        
            for x in range(0, len(num_str), 1):
                if int(num_str[x]) == total - int(num_str[x]):
                    # print("DS number found: " + num_str)
                    return True
            
            return False
        
        '''
        is_ds_num("3003")
        is_ds_num("352")
        is_ds_num("32812")
        DS number found: 3003
        DS number found: 352
        DS number found: 32812
        '''

        def solve(N):
            str_map = project_euler_725_STR_HM.STRING_MAP
            sum_map = project_euler_725_SUM_HM.SUM_HM

            sum = 0
            for n in range(1, N+1, 1):
                check_hm = sum_map.get(n)
                if sum_map.get(n) is None:
                    n_digit_strs = generate_all_n_digit_strings(n, str_map)
                    for x in range(0, len(n_digit_strs), 1):
                        if is_ds_num(n_digit_strs[x]):
                            sum += int(n_digit_strs[x])
                    sum_map[n] = sum
                    print("Completing: " + str(n) + " sum: " + str(sum))
                else:
                    sum += check_hm
            
            print("Solution found: " + str(sum))
            print(sum_map)
            print("")
            print(str_map)

        #solve(2) # Solution found: 495
        #solve(3) # Solution found: 63270
        #solve(4) # Solution found: 3149685
        #solve(5) # Solution found: 112398876
        #solve(6) # Solution found: 3311663355
        #solve(7) # Solution found: 85499991450
        solve(100)
        #solve(2020)

    except Exception as ex:

        print('Exception: ' + str(ex))