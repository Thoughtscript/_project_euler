
# https://www.mathsisfun.com/prime-factorization.html
# https://www.geeksforgeeks.org/prime-factor/
# https://www.math.drexel.edu/~tolya/220_euclid.pdf

prime factorization

# So, all numbers are either primes or not.
# All primes are divisible only by themselves and 1.
# All non-primes can actually be represented as prime factors! (E.g. - they are composite numbers.)

# Divide a number n by 2 repeatedly until it can't be cleanly divided.
# Note that dividing by 2 cleanly until it can't be done anymore results in only odd divisors
# Then continue to check through the next primes in the same way until the total amount of all primes multiplied together is greater than n.

# 12 is 2 x 2 x 3
# 18 is 2 x 3 x 3

# ---------------------------------- #

# https://www.geeksforgeeks.org/sieve-of-eratosthenes/
# https://byjus.com/maths/sieve-of-eratosthenes/

Sieve of Eratosthenes

# 1. Define an array of length n equal to the target max number. Init each value to true or false (for is prime or not).
# 2. Each non-prime number will have at least one other divisor besides itself and 1. 
# 3. So, by finding every multiple of i from 1 to n (for each i), one can quickly identify any non-primes! (Divisible by i and >= to the square of i - the second clause prevents numbers from being checked twice.)
# 4. The remaining numbers are primes.

# ---------------------------------- #

# https://www.geeksforgeeks.org/total-number-divisors-given-number/
# https://www.geeksforgeeks.org/count-divisors-n-on13/
# https://www.math.drexel.edu/~tolya/220_euclid.pdf
# https://www.wikihow.com/Determine-the-Number-of-Divisors-of-an-Integer

number of divisors

# 1. Use the Sieve of Eratosthenes
# 2. Find all prime factors for n.
# 3. Multiple each prime factor exponent adding one to each multiple 1: d(24) = (3+1)(1+1) = 2 x 2 x 2 x 3
# 4. So, there are 8 divisors for 24: 1,2,3,4,6,8,12,24