# https://projecteuler.net/problem=66


if __name__ == '__main__':

    try:

        def is_diophantine(x, d, y):
            return pow(x, 2) - d * pow(y, 2) == 1
        
        def is_integer(x, y):
            return int(x) == y
        
        def solve():
            # 61 is not known with certainty
            hm = {2: 3, 3: 2, 5: 9, 6: 5, 7: 8, 8: 3, 10: 19, 11: 10, 12: 7, 13: 649, 14: 15, 15: 4, 17: 33, 18: 17, 19: 170, 20: 9, 21: 55, 22: 197, 23: 24, 24: 5, 26: 51, 27: 26, 28: 127, 29: 9801, 30: 11, 31: 1520, 32: 17, 33: 23, 34: 35, 35: 6, 37: 73, 38: 37, 39: 25, 40: 19, 41: 2049, 42: 13, 43: 3482, 44: 199, 45: 161, 46: 24335, 47: 48, 48: 7, 50: 99, 51: 50, 52: 649, 53: 66249, 54: 485, 55: 89, 56: 15, 57: 151, 58: 19603, 59: 530, 61: 335159612, 60: 31, 62: 63, 63: 8, 65: 129, 66: 65, 67: 48842, 68: 33, 69: 7775, 70: 251, 71: 3480, 72: 17, 73: 2281249, 74: 3699, 75: 26, 76: 57799, 77: 351, 78: 53, 79: 80, 80: 9, 82: 163, 83: 82, 84: 55, 85: 285769, 86: 10405, 87: 28, 88: 197, 89: 500001, 90: 19, 91: 1574, 92: 1151, 93: 12151, 94: 2143295, 95: 39, 96: 49, 97: 62809633, 98: 99, 99: 10, 101: 201, 102: 101, 103: 227528, 104: 51, 105: 41, 106: 32080051, 107: 962, 108: 1351, 109: 181718045, 110: 21, 111: 295, 112: 127, 113: 1204353, 114: 1025, 115: 1126, 116: 9801, 117: 649, 118: 306917, 119: 120, 120: 11, 122: 243, 123: 122, 124: 4620799, 125: 930249, 126: 449, 127: 4730624, 128: 577, 129: 16855, 130: 6499, 131: 10610, 132: 23, 133: 2588599, 134: 145925, 135: 244, 136: 35, 137: 6083073, 138: 47, 139: 77563250, 140: 71, 141: 95, 142: 143, 143: 12, 145: 289, 146: 145, 147: 97, 148: 73, 149: 255105526}

            max_x = -1
            for d in range(1, 250, 1):
                sq_rt = pow(d, 1/2)
                if is_integer(sq_rt, sq_rt):
                    print("Skipping: " + str(d) + " as it's a square")
                    continue

                else:
                    get_hm_val = hm.get(d)
                    if not get_hm_val is None:
                        max_x = max(max_x, get_hm_val)
                        continue

                    print("Trying D: " + str(d))
                    found = False
                    for x in range(1, 999999999, 1):
                        # Try q as x to find a valid y
                        a = 1 - pow(x, 2)
                        y = pow(a / -d, 1/2)
                        if is_integer(y, y) and y > 0:
                            print("Minimal Diophantine X found: " + str(x) + " for eq: " + str(x) + "^2- " + str(d) + " * " + str(int(y)) + "^2 =1")
                            hm[d] = int(x)
                            max_x = max(max_x, x)
                            found = True
                            break
                    
                    if not found:
                        raise Exception("No Minimal Diophantine found")

            print("Max X found: " + str(max_x))
            print(hm)
        
        '''
        Minimal Diophantine X found: 3 for eq: 3^2-2*2^2=1
        Minimal Diophantine X found: 2 for eq: 2^2-3*1^2=1
        Minimal Diophantine X found: 9 for eq: 9^2-5*4^2=1
        Minimal Diophantine X found: 5 for eq: 5^2-6*2^2=1
        Minimal Diophantine X found: 8 for eq: 8^2-7*3^2=1
        '''

        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))