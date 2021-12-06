# https://projecteuler.net/problem=19

import datetime

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

        # Iterate Months
        # Check if 1st of Month is a Sunday

        # Iterate Years
        # Between 1/1/1901 to 12/31/2000

        def solve():
            count = 0
            for year in range(1901,2001,1):
                for month in range(1,13,1):
                    d = datetime.datetime(year, month, 1)
                    if d.strftime('%A') == 'Sunday':
                        count = count + 1
                        print("Found: " + str(d) + " is a " + d.strftime('%A'))
            
            print(count)
            return count

        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))