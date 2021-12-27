# https://projecteuler.net/problem=23

if __name__ == '__main__':

    try:

        def proper_divisors_of(num):
            divisors = []

            for x in range(1, num, 1):
                if num % x == 0:
                    divisors.append(x)

            # print(divisors)
            return divisors

        # proper_divisors_of(28) # [1, 2, 4, 7, 14]

        def sum_array(arr):
            result = 0

            for x in range(0, len(arr), 1):
                result = result + arr[x]

            return result

        # If False and equal it's neither abundant nor deficient. It's perfect.
        # If False, it's not deficient
        def is_abundant(num):
            divisors = proper_divisors_of(num)
            sum = sum_array(divisors)

            if sum > num:
                return True

            # if sum == num:
                # print("Neither abundant nor deficient. It's perfect.")

            return False

        # ------------------------------------------------ #

        def find_all_abundant():
            abundant_numbers = []

            for x in range(1, 28123 + 1, 1):
                if is_abundant(x):
                    abundant_numbers.append(x)

            # print(abundant_numbers)
            return abundant_numbers

        def generate_answer_space():
            abundant_numbers = find_all_abundant()
            LEN = len(abundant_numbers)
            hm = {}

            for i in range(0, LEN, 1):
                I = abundant_numbers[i]
                for j in range(0, LEN, 1):
                    J = abundant_numbers[j]

                    if I + J > 28123:
                        break

                    hm[I + J] = True

            print(hm)
            return hm

        def solve():
            not_two_abundant_nums = []
            hm = generate_answer_space()

            # All numbers above 28123 are known to be 
            # writeable as the sum of two abundant numbers.
            for x in range(1, 28124, 1):
                n = hm.get(x)
                if n is None:
                    print(str(x) + " cannot be expressed as the sum of two abundant numbers.")
                    not_two_abundant_nums.append(x)

            print(not_two_abundant_nums)
            result = sum_array(not_two_abundant_nums)
            print(result)
            return result

        solve() # 4179871

    except Exception as ex:

        print('Exception: ' + str(ex))
