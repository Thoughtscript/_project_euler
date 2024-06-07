# https://projecteuler.net/problem=243

from decimal import *
import primes_to_50_mil as PRIMES

if __name__ == '__main__':

    try:
        def euler_totient_fun(n, pfs):
            result = Decimal(n)

            # n * (1-(1/pfs[0])) * (1-(1/pfs[1])) ... 
            for x in range(0, len(pfs), 1):
                pf = Decimal(pfs[x])
                result *= Decimal(Decimal(1) - (Decimal(1)/pf))

            return result
    

        # Do unique pfs generate new valid numbers?
        def solve():
            target = Decimal(15499) / Decimal(94744)
            num = 1
            denom = 2
            pfs = [2]

            L = len(PRIMES.primes)

            for x in range(1, L, 1):
                p = PRIMES.primes[x]
                num *= p
                denom *= p
                pfs.append(p)
                totient = euler_totient_fun(denom, pfs)
                ratio = Decimal(totient) / Decimal(denom - 1)
                if ratio < target:
                    print("A smaller solution found: " + str(ratio) + " d: " + str(denom) + " pfs: " + str(pfs))
                    break

        solve()
                                         
    except Exception as ex:

        print('Exception: ' + str(ex))