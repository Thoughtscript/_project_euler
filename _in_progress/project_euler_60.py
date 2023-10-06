# https://projecteuler.net/problem=60

import primes_to_5_mil as P

if __name__ == '__main__':

    try:

        def sum_set(arr):
            sum = 0
            for x in range(0, len(arr), 1):
                sum = sum + arr[x]
            return sum

        def prime_map():
            primes = {}

            for x in range(0, len(P.primes), 1):
                primes[P.primes[x]] = True
            
            return primes

        def solve(slice_num):
            PRIMES = P.primes[0:slice_num]
            PRIME_MAP = prime_map()
            PRIMES.sort()
            hm = {}

            LEN = len(PRIMES)

            for x in range(0, LEN, 1):

                for y in range(0, LEN, 1):
                    if x == y:
                        continue

                    for z in range(0, LEN, 1):
                        if z == x or z == y:
                            continue

                        for w in range(0, LEN, 1):
                            if w == x or w == y or w == z:
                                continue

                            for q in range(0, LEN, 1):
                                if q == w or q == z or q == y or q == x:
                                    continue

                                arr = []
                                arr.append(PRIMES[x])
                                arr.append(PRIMES[y])
                                arr.append(PRIMES[z])
                                arr.append(PRIMES[w])
                                arr.append(PRIMES[q])

                                flag = True
                                print("Trying " + str(arr))

                                for a in range(0, 4, 1):
                                    for b in range(0, 4, 1):
                                        if a == b:
                                            continue

                                    str_a = str(arr[a]) + str(arr[b])
                                    str_b = str(arr[b]) + str(arr[a])

                                    A = PRIME_MAP.get(int(str_a))
                                    B = PRIME_MAP.get(int(str_b))

                                    if not A == None and not B == None:
                                        continue
                                    else:
                                        flag = False
                                        break
                                
                                if flag:
                                    print("Set found!")
                                    print(arr)
                                    print(sum_set(arr))
                                    return sum_set(arr)

            print("None found!")

        solve(250) # > 25

    except Exception as ex:

        print('Exception: ' + str(ex))