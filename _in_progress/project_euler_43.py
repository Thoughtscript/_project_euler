# https://projecteuler.net/problem=43

if __name__ == '__main__':

    try:

        # Same set of triples is use for each 3-length sub-strings.
        # Generate once and use for all.
        def make_triples():
            result = []

            for a in range(0, 10, 1):
                for b in range(0, 10, 1):
                    if a == b:
                        continue

                    for c in range(0, 10, 1):
                        if a == c or b == c:
                            continue

                        result.append(str(a) + str(b) + str(c))
            
            # print(result)
            # print(len(result)) # 720 - should be factorial 10 x 9 x 8
            return result

        TRIPLES = make_triples()

        def includes(a, b):
            num_str = str(a)
            for x in range(0, len(num_str), 1):
                if int(num_str[x]) == int(b):
                    return True
            return False

        # Cannot brute force the strings above: 10 x 720 x 720 x 720.
        # Must use string compression (or something faster): 3,628,800 vs. 3,732,480,000.
        def make_strings():
            result = []

            LEN = len(TRIPLES)

            for x in range(0, 10, 1):

                for a in range(0, LEN, 1):
                    A = TRIPLES[a]

                    if includes(A, x):
                        continue

                    for b in range(0, LEN, 1):
                        B = TRIPLES[b]

                        if a == b:
                            continue

                        if includes(B, x):
                            continue

                        found = False

                        for y in range(0, len(B), 1):
                            if includes(A, B[y]):
                                found = True
                                break

                        if found:
                            continue

                        for c in range(0, LEN, 1):
                            C = TRIPLES[c]

                            if a == c or b == c:
                                continue

                            if includes(C, x):
                                continue

                            found = False

                            for z in range(0, len(C), 1):
                                if includes(B, C[z]) or includes(A, C[z]):
                                    found = True
                                    break

                            if found:
                                continue

                            num_str = str(x) + A + B + C
                            print("String made: " + str(num_str))
                            result.append(int(num_str))

            print(result)
            return result

        NUM_STRINGS = make_strings()

        def is_pandigital(num):
            num_str = str(num)

            hm = {}

            for x in range(0, len(num), 1):
                n = num[x]
                check = hm.get(n)
                if check is None:
                    hm[n] = True
                else:
                    return False

            # d2d3d4 is d1d2d3 offset by 1!
            if not int(num_str[1] + num_str[2] + num_str[3]) % 2 == 0:
                return False

            if not int(num_str[2] + num_str[3] + num_str[4]) % 3 == 0:
                return False

            if not int(num_str[3] + num_str[4] + num_str[5]) % 5 == 0:
                return False

            if not int(num_str[4] + num_str[5] + num_str[6]) % 7 == 0:
                return False

            if not int(num_str[5] + num_str[6] + num_str[7]) % 11 == 0:
                return False

            if not int(num_str[6] + num_str[7] + num_str[8]) % 13 == 0:
                return False

            if not int(num_str[7] + num_str[8] + num_str[9]) % 17 == 0:
                return False

            return True

        # ------------------------------------ #

        def solve():
            count = 0

            for x in range(0, len(NUM_STRINGS), 1):
                check = is_pandigital(NUM_STRINGS[x])
                if check:
                    count = count + 1

            print("Pandigital Numbers found: " + str(count))
            return count
        

    except Exception as ex:

        print('Exception: ' + str(ex))