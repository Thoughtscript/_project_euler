# https://projecteuler.net/problem=58

# Better analysis 
## My own original analysis to simplify by just generating the diags!!!!

# [65, 64, 63, 62, 61, 60, 59, 58, 57], 
# [66, 37, 36, 35, 34, 33, 32, 31, 56], 
# [67, 38, 17, 16, 15, 14, 13, 30, 55], 
# [68, 39, 18, 5, 4, 3, 12, 29, 54], 
# [69, 40, 19, 6, 1, 2, 11, 28, 53], 
# [70, 41, 20, 7, 8, 9, 10, 27, 52], 
# [71, 42, 21, 22, 23, 24, 25, 26, 51], 
# [72, 43, 44, 45, 46, 47, 48, 49, 50],
# [73, 74, 75, 76, 77, 78, 79, 80, 81]

# [37, 36, 35, 34, 33, 32, 31], 
# [38, 17, 16, 15, 14, 13, 30], 
# [39, 18, 5, 4, 3, 12, 29], 
# [40, 19, 6, 1, 2, 11, 28], 
# [41, 20, 7, 8, 9, 10, 27], 
# [42, 21, 22, 23, 24, 25, 26], 
# [43, 44, 45, 46, 47, 48, 49]

# [17, 16, 15, 14, 13],
# [18, 5, 4, 3, 12], 
# [19, 6, 1, 2, 11], 
# [20, 7, 8, 9, 10], 
# [21, 22, 23, 24, 25]

# UR: 1, 3, 13, 31, 57
##      2, 10, 18, 26 -> increases by 8 (2nd Order Derivative)
# UL: 1, 5, 17, 37, 65
##      4  12  20  28 -> increases by 8 (2nd Order Derivative)
# LL: 1, 7, 21, 43, 73
##      6  14  22  30 -> increases by 8 (2nd Order Derivative)
# LR: 1, 9, 25, 49, 81
##      8  16  24  32 -> increases by 8 (2nd Order Derivative)

if __name__ == '__main__':

    import primes_to_50_mil

    try:   
        def prime_map():
            primes = {}

            for x in range(0, len(primes_to_50_mil.primes), 1):
                primes[primes_to_50_mil.primes[x]] = True
            
            return primes
        
        PRIME_MAP = prime_map()

        def is_prime(x):
            return not PRIME_MAP.get(x) is None
        
        def expand_by_one_layer(dul, dll, dlr, dur, ul, ll, lr, ur):
            dul = dul + 8
            dll = dll + 8
            dlr = dlr + 8
            dur = dur + 8

            nul = ul[len(ul)- 1] + dul
            nll = ll[len(ll)- 1] + dll
            nlr = lr[len(lr)- 1] + dlr
            nur = ur[len(ur)- 1] + dur
            
            ul.append(nul)
            ll.append(nll)
            lr.append(nlr)
            ur.append(nur)

            return [nul, nll, nlr, nur]
        
        def calcDiags(nul, nll, nlr, nur, ps, nps):
            if not is_prime(nul):
                nps += 1
            else:
                ps += 1

            if not is_prime(nlr):
                nps += 1
            else:
                ps += 1

            if not is_prime(nll):
                nps += 1
            else:
                ps += 1

            if not is_prime(nur):
                nps += 1
            else:
                ps += 1

            percent = ps / (ps + nps)
            print("count_primes " + str(ps) + " count_non_primes " + str(nps) + " % " + str(percent))
            return [ps, nps, percent]

        def solve():
            dul = 20
            dll = 22
            dlr = 24
            dur = 18

            ps = 8
            nps = 5
    
            ul = [1, 5, 17, 37]
            ll = [1, 7, 21, 43]
            lr = [1, 9, 25, 49]
            ur = [1, 3, 13, 31]

            sidelength = 7

            for layer in range(0, 999999999, 1):
                # print("Layer " + str(layer))
                # print(ul)
                # print(ll)
                # print(lr)
                # print(ur)

                [nul, nll, nlr, nur] = expand_by_one_layer(dul, dll, dlr, dur, ul, ll, lr, ur)
                [p, np, percent] = calcDiags(nul, nll, nlr, nur, ps, nps)
                ps = p
                nps = np
                sidelength += 2

                if percent < .1:
                    print("Solution found at layer: " + str(layer) + " with side_length: " + str(sidelength))
                    break
        
        solve() # I run out of primes

    except Exception as ex:

        print('Exception: ' + str(ex))