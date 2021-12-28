# https://projecteuler.net/problem=73

if __name__ == '__main__':

    try:

        def reduced_proper_fraction(n, d):
            # TBD
            if n < d and False:
                return True
            return False

        def solve():

            hm = {}

            # 1/3 to 1/2
            # 4000/12000 to 6000/12000
            d = 12000

            for n in range(4000, 6001, 1):
                if reduced_proper_fraction(n, d):
                    hm[]

            print(hm)
            print(len(hm.keys))
            return len(hm.keys)


    except Exception as ex:

        print('Exception: ' + str(ex))