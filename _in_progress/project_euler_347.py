# https://projecteuler.net/problem=347

import primes_to_5_mil as P

if __name__ == '__main__':

    try:

        primes = P.primes

        def m(p,q,N):
            largest = 0

            for X in range(0, N+1, 1):
                if X % p == 0 and X % q == 0 and not p == q:

                    third_found = False

                    for y in range(0, len(primes), 1):
                        prime = primes[y]

                        if prime == p or prime == q:
                            continue
    
                        if prime > X:
                            break

                        if X % prime == 0:
                            third_found = True
                            break

                    if not third_found:
                        # print("New largest integer found: " + str(X))
                        largest = max(largest, X)
            
            if largest > 0:
                print("Largest integer found that's divisible by only the two primes: " + str(p) + " and " + str(q) + " = " + str(largest))
            return largest
        

        # m(2,3,100) # Largest integer found that's divisible by only the two primes: 2 and 3 = 96
        # m(3,5,100) # Largest integer found that's divisible by only the two primes: 3 and 5 = 75
        # m(2,73,100) # 0
    
        def solve(mx):
            total_score = 0

            for x in range(0, len(primes), 1):
                if primes[x] > mx:
                    break

                for y in range(0, len(primes), 1):
                    if primes[y] > mx:
                        break

                    if primes[x] == primes[y]:
                        continue

                    total_score += m(primes[x],primes[y], mx)

            total_score = total_score / 2
            print("Total Score for: " + str(mx) + " is: " + str(total_score))
        
        # solve(100) # Total Score for: 100 is: 2262.0

        #solve(10000000)

    except Exception as ex:

        print('Exception: ' + str(ex))