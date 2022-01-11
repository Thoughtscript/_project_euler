# https://projecteuler.net/problem=33

from decimal import *

if __name__ == '__main__':

    try:
        
        def solve():
            non_trivial = []

            max_val = 100
            # numerator and denominator must both have two digits
            for numerator in range(10, max_val, 1):
                num_str = str(numerator)

                for denominator in range(10, max_val, 1):
                    den_str = str(denominator)

                    fraction = Decimal(numerator) / Decimal(denominator)
                    if fraction >= 1:
                        continue

                    if not int(den_str[1]) == 0 and fraction == Decimal(int(num_str[0])) /  Decimal(int(den_str[1])) and int(num_str[1]) == int(den_str[0]):
                        print("Non-trivial cancelling fraction found: " + num_str + "/" + den_str)
                        non_trivial.append(fraction)

                    if not int(den_str[0]) == 0 and  fraction == Decimal(int(num_str[1])) /  Decimal(int(den_str[0])) and int(num_str[0]) == int(den_str[1]):
                        print("Non-trivial cancelling fraction found: " + num_str + "/" + den_str)
                        non_trivial.append(fraction)

            print(non_trivial)

            product = Decimal(1)

            for x in range(0, len(non_trivial), 1):
                product = product * non_trivial[x]

            print(product) # 0.01000
            return non_trivial


        solve() # 1/100 -> 100 is the denominator


    except Exception as ex:

        print('Exception: ' + str(ex))