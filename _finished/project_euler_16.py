# https://projecteuler.net/problem=16

if __name__ == '__main__':

    try:

        num = pow(2, 1000)
        print(num)
        st = str(num)
        sm = 0

        for x in range(0, len(st), 1):
            sm = int(st[x]) + sm

        print(sm) # 1366

    except Exception as ex:
        print('Exception: ' + str(ex))