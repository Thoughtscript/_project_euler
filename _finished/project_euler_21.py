# https://projecteuler.net/problem=21

if __name__ == '__main__':

    try:

        def d(n):
            divisors = []

            for x in range(1, n, 1):
                if n % x == 0:
                    divisors.append(x)

            # print(divisors)

            sum = 0

            for x in range(0, len(divisors), 1):
                sum = sum + divisors[x]

            # print(sum)
            return sum

        # d(220) #284
        # d(284) #220

        def generate(mx):
            hm = {}

            for x in range(1, mx+1, 1):
                hm[x] = d(x)

            print(hm)
            return hm

        def amicable_pair(x, y):
            if x == d(y) and y == d(x) and not x == y and not y == x:
                return [True, x + y]
            return [False, 0]

        # print(amicable_pair(220, 284))

        def solve(mx):
            hm = generate(mx)

            keys = hm.keys()
            found = {}
            sum = 0

            for x in range(0, len(keys), 1):
                for y in range(0, len(keys), 1):
                    if (x == hm.get(y) and y == hm.get(x) and not x == y and not y == x):
                        if found.get(str(x) + str(y)) is None:                        
                            print("Amicable Pair found: " + str(x) + " " + str(y))
                            sum = sum + x + y
                            found[str(x) + str(y)] = True
                            found[str(y) + str(x)] = True
                        else:
                            print("Pair already found")

            print(sum)
            return sum

        solve(10000)

        # Amicable Pair found: 220 284
        # Pair already found
        # Amicable Pair found: 1184 1210
        # Pair already found
        # Amicable Pair found: 2620 2924
        # Pair already found
        # Amicable Pair found: 5020 5564
        # Pair already found
        # Amicable Pair found: 6232 6368
        # Pair already found
        # 31626

    except Exception as ex:

        print('Exception: ' + str(ex))