# https://projecteuler.net/problem=19

if __name__ == '__main__':

    try:

        def is_leap_year(year):
            if not year % 4 == 0:
                return False

            if year % 100 == 0 and not year % 400 == 0:
                return False

            return (year % 4 == 0 and year % 400 == 0)

        #print(is_leap_year(2000))
        #print(is_leap_year(2400))
        #print(is_leap_year(1800))
        #print(is_leap_year(1900))
        #print(is_leap_year(2200))

        def solve():
            # Iterate Months
            # Check if 1st of Month is a Sunday

            # Iterate Years
            # Between 1/1/1901 to 12/31/2000
            return

        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))