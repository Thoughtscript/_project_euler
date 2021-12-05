# https://projecteuler.net/problem=25

import sys

if __name__ == '__main__':

    # This ended up being more of an exercise in the basis of Python than Fib. numbers LOL.
    # Python has a defuault max recursion limit - I've never hit that before. Even my machine learning algos terminate in < 100 calls and/or don't use recursion.
    # Also, Python has no Max Int or Big Int equivalent. Useful for Project Euler so I'll be using Python going forward.
    # Solution below is little more memory efficient since it uses a constantly-sized array of length 2.

    def set_recursion_limit(n):
        sys.setrecursionlimit(n)
        # print(sys.getrecursionlimit())

    def reset_recursion_limit():
        sys.setrecursionlimit(1000)
        # print(sys.getrecursionlimit())

    try:

        def innerFib(arr, target, current):
            L = len(arr)
            N = arr[L - 2] + arr[L - 1]

            if len(str(N)) >= 1000:
                print('First number with string length greater than or equal to 1000 found: ' + str(N) + " it's number " + str(current) + "\n")
                return N

            arr[0] = arr[L - 1]
            arr[1] = N

            if current < target:
                current = current + 1
                innerFib(arr, target, current)
            else:
                L = len(arr)
                # print(arr)
                print(str(current) + '-nth number is ' + str(arr[L - 1]))
                print('Length of string representation is ' + str(len(str(arr[L - 1]))) + '\n')

        def fibonacci(target):
            MN = 1
            if target <= MN:
                print('Please enter a number greater than ' + MN)
            else:
                innerFib([0,1], target, MN + 1)

        set_recursion_limit(10000)

        # fibonacci(3) # 3-nth number is 2

        # fibonacci(8) # 8-nth number is 21

        # fibonacci(35) # 35-nth number is 9227465

        # fibonacci(992) # 992-nth number is 925239415994386554869588530526732113391791027107146089675782213997604728132159099144675176879829352818608730653883769505215818615700996374793242741022444070914268567004041261931970004460258737885521082308229

        # fibonacci(2000) # 2000-nth number is 4224696333392304878706725602341482782579852840250681098010280137314308584370130707224123599639141511088446087538909603607640194711643596029271983312598737326253555802606991585915229492453904998722256795316982874482472992263901833716778060607011615497886719879858311468870876264597369086722884023654422295243347964480139515349562972087652656069529806499841977448720155612802665404554171717881930324025204312082516817125

        # fibonacci(1050) # 1050-nth number is 1223312068647805695866041001606414215425662481984418699889280184734522565471193888244259842002003203662301235495264496143544059342859868972795832692060911690562863420044109984978877398486541422811217041686547085400321400

        # fibonacci(1750) # 1750-nth number is 239268449498292362938407468767876856840297041399432969414967451110574171482470078416105732791272420373102851043141132269799332415847948407421782374884222348578539240203259231738617166890796312443015896962903711399287947211016568314077204856553633339146474734051327758449261017199508247968021562405485128344479531129615452456857458382425794168471705417336645711603375

        fibonacci(4782)

        fibonacci(9000)

        reset_recursion_limit()

    except Exception as ex:

        print('Exception: ' + str(ex))