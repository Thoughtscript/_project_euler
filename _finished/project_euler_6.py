# https://projecteuler.net/problem=6

if __name__ == '__main__':

    try:
        def sum_of_squares(top):
            result = 0
            for x in range(1,top+1,1):
                result = result + pow(x, 2)

            print(result)
            return result

        def square_of_sums(top):
            result = 0
            for x in range(1,top+1,1):
                result = result + x
            
            result = pow(result, 2)
            print(result)
            return result

        print(sum_of_squares(100) - square_of_sums(100)) # 25164150

    except Exception as ex:
        print('Exception: ' + str(ex))