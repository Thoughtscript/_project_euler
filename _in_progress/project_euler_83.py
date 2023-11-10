# https://projecteuler.net/problem=83
import copy
import sys

if __name__ == '__main__':

    try:

        def set_recursion_limit(n):
            sys.setrecursionlimit(n)

        def reset_recursion_limit():
            sys.setrecursionlimit(1000)

        N = 80

        def init():
            result_array = []
            fileHandler = open('project_euler_83_input.txt')
            for line in fileHandler:
                result_array.append(line.split(","))
            # print(result_array)
            return result_array
        
        def check_cell(orig_matrix, row, col, total, visited, totals):
            new_visited = copy.deepcopy(visited)
            new_visited[str(row)+"-"+str(col)] = True
            curr_cell = int(orig_matrix[row][col])
            new_total = curr_cell + total
            if row == N-1 and col == N-1:
                # print(new_total)
                totals.append(new_total)
                return
            
            has_left = col - 1 >= 0
            has_right = col + 1 < N
            has_above = row - 1 >= 0
            has_below = row + 1 < N

            if has_left and visited.get(str(row)+"-"+str(col - 1)) is None:
                check_cell(orig_matrix, row, col-1, new_total, new_visited, totals) # l

            if has_above and visited.get(str(row - 1)+"-"+str(col)) is None:
                check_cell(orig_matrix, row-1, col, new_total, new_visited, totals) # u

            if has_right and visited.get(str(row)+"-"+str(col + 1)) is None:
                check_cell(orig_matrix, row, col+1, new_total, new_visited, totals) # r

            if has_below and visited.get(str(row + 1)+"-"+str(col)) is None:
                check_cell(orig_matrix, row+1, col, new_total, new_visited, totals) # d

        def solve():
            totals = []
            check_cell(init(), 0, 0, 0, {}, totals)
            print("Minimum solution found: " + str(min(totals))) 

        set_recursion_limit(99999)

        solve() # Minimum solution found: 28105

        '''
        131,673,234,103,18
        201,96,342,965,150
        630,803,746,422,111
        537,699,497,121,956
        805,732,524,37,331

        Minimum solution found: 2297 - correct answer
        '''

        reset_recursion_limit()

    except Exception as ex:

        print('Exception: ' + str(ex))