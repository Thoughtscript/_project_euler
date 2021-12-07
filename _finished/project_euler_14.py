# https://projecteuler.net/problem=14

if __name__ == '__main__':

    try:

        def sequence(num):
            result = []

            while True:
                result.append(num)

                if num == 1:
                    break

                if num % 2 == 0:
                    num = num / 2
                else:
                    num = 3 * num + 1
                

            #print(result)
            return result

        #sequence(13)
        #sequence(45)
        #sequence(20000)

        def solve(num):
            mx = 0
            n = -1

            for x in range(1,num,1):
                s = sequence(x)
                if len(s) > mx:
                    mx = len(s)
                    n = x
                    print("New max found: " + str(s) + " number: " + str(x))
                    print("\n")
            
            print("Final number: " + str(n))
            return n

        solve(1000000)

    except Exception as ex:
        print('Exception: ' + str(ex))