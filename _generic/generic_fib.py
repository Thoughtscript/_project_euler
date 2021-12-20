# Generic Fib.

if __name__ == '__main__':

    try:

        def innerFib(arr, n, current):
            if (current < 2):
                arr.append(current)
            else:
                arr.append(arr[current - 2] + arr[current - 1])

            if (current < n):
                current = current + 1
                innerFib(arr, n, current)
            else:
                L = len(arr)

                # All generated numbers
                print(arr)

                # Last number
                print('Last number: ' + str(arr[L - 1]))

                # Total numbers
                print('Total numbers: ' + str(L))

                # Nth number
                print(str(L) + '-th number is ' + str(arr[L - 1]))
                
                # Length of number in string representation
                print('Length of digit as string: ' + str(len(str(arr[L - 1]))) + '\n')

        def fibonacci(n):
            innerFib([], n, 0)

        fibonacci(10)
        # fibonacci(100)
        # fibonacci(990)

    except Exception as ex:

        print('Exception: ' + str(ex))