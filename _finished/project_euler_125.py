# https://projecteuler.net/problem=125

'''
100 000 000 - max length 9 palindrome string
'''

if __name__ == '__main__':

    try:

        def generate_all_odd_palindromes_of_length(n):
            last_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            counter = 1

            while counter < n:
                temp = []
                for x in range(0, len(last_array), 1):
                    for y in range(0, 10, 1):
                        temp.append(str(y) + str(last_array[x]) + str(y))
                        #print(str(y) + str(last_array[x]) + str(y))
                last_array = temp
                counter += 2

            return last_array

        # YAAY -> Y AA Y
        # YA - AY
        # These are identical
        def generate_all_even_palindromes_of_length(n):
            last_array = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"]
            counter = 2

            while counter < n:
                temp = []
                for x in range(0, len(last_array), 1):
                    for y in range(0, 10, 1):
                        temp.append(str(y) + str(last_array[x]) + str(y))
                        #print(str(y) + str(last_array[x]) + str(y))
                last_array = temp
                counter += 2


            #print(last_array)
            return last_array
        
        #generate_all_even_palindromes_of_length(4)

        def check_cons_square(num_str, max_num):
            if num_str[0] == "0":
                return 0
            
            num_num = int(num_str)
            if num_num >= max_num:
                return 0

            for x in range(1, num_num, 1):
                total = 0
                squares = []
                if pow(x, 2) > num_num:
                    break

                for y in range(x, num_num, 1):
                    total += pow(y, 2)
                    squares.append(y)
                    if total > num_num:
                        break
                    if total == num_num and len(squares) > 1:
                        print("Palindromic Consecutive square found: " + num_str)
                        print(squares)
                        return num_num
            return 0
        
        #check_cons_square("595")

        def solve(max_num):
            num_str = str(max_num)
            total = 0
            pals =  ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"] + ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for x in range(3, len(num_str) + 1, 1):
                if x % 2 == 0:
                    pals = pals + generate_all_even_palindromes_of_length(x)
                else:
                    pals = pals + generate_all_odd_palindromes_of_length(x)

            # print(pals)

            for x in range(0, len(pals), 1):
                total += check_cons_square(pals[x], max_num)

            print("Solution found: " + str(total))

        solve(100000000) # 2906969179

        '''
        solve(1000)

        Palindromic Consecutive square found: 505
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        Palindromic Consecutive square found: 313
        [12, 13]
        Palindromic Consecutive square found: 818
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        Palindromic Consecutive square found: 434
        [11, 12, 13]
        Palindromic Consecutive square found: 636
        [4, 5, 6, 7, 8, 9, 10, 11, 12]
        Palindromic Consecutive square found: 545
        [16, 17]
        Palindromic Consecutive square found: 181
        [9, 10]
        Palindromic Consecutive square found: 595
        [6, 7, 8, 9, 10, 11, 12]
        Palindromic Consecutive square found: 5
        [1, 2]
        Palindromic Consecutive square found: 55
        [1, 2, 3, 4, 5]
        Palindromic Consecutive square found: 77
        [4, 5, 6]
        Solution found: 4164
        '''


    except Exception as ex:

        print('Exception: ' + str(ex))