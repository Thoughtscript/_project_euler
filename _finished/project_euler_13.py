# https://projecteuler.net/problem=13
import json

if __name__ == '__main__':

    try:

        def init():
            jsonAsString = ""
            fileHandler = open('project_euler_13_data.json')
            for line in fileHandler:
                jsonAsString += line
            entries = json.loads(jsonAsString)
            # print(entries)
            return entries

        def solve(arr):
            sum = 0
            for x in range(0, len(arr),1):
                sum = sum + arr[x]
            print(sum)
            return sum

        solve(init()) # 5537376230390876637302048746832985971773659831892672
        # 55373 76230 
    except Exception as ex:

        print('Exception: ' + str(ex))