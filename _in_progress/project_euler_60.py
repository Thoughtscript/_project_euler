# https://projecteuler.net/problem=60

if __name__ == '__main__':

    try:

        def count_digits(num_str):
            hm = [0,0,0,0,0,0,0,0,0,0]

            for x in range(0, len(num_str), 1):
                key = int(num_str[x])
                hm[key] = hm[key] + 1
            
            return hm

        def compare(a, b):
            A = a.keys()
            B = b.keys()

            for x in range(0, len(A), 1):
                if a.get(A[x]) == b.get(B[x]):
                    continue
                else:
                    return False

            return True

        def solve():

            for x in range(0, 1000000, 1):
                hm_x = count_digits(str(x))

                for y in range(2,7,1):
                    z = y * z
                    hm_z = count_digits(str(y))
                    if compare(hm_x, hm_z):
                        print("Number found: " + str(x))

            print("No number found!")
            return
            

        solve()
     
    except Exception as ex:

        print('Exception: ' + str(ex))