# https://projecteuler.net/problem = 67

if __name__ == '__main__':

    try:

        def parse(file_name):
            result_arr = []
            file_handler = open(file_name)

            for line in file_handler:
                cleaned = line.replace('\n', '').split(" ")

                for x in range(0, len(cleaned), 1):
                    cleaned[x] = int(cleaned[x])

                result_arr.append(cleaned)
                # print(cleaned)

            print(result_arr)
            return result_arr

        DATA = parse('project_euler_67_input.txt')

        def check_below(r, c):
            next_row = r + 1
            same_col = c
            next_col = c + 1
            DATA[r][c] =  DATA[r][c] + max(DATA[next_row][same_col], DATA[next_row][next_col])

        def solve():

            for r in range(len(DATA) - 2, -1, -1):
                for c in range(0, len(DATA[r]), 1):
                    check_below(r, c)

            print(DATA)
            print(DATA[0][0])
            return DATA[0][0]

        solve() # 7273

        # Start from bottom up:
        # DATA[r-1][c] += Math.max(DATA[r][c], DATA[r][c+1])

    except Exception as ex:

        print('Exception: ' + str(ex))
