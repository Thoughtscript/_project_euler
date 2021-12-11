# https://projecteuler.net/problem=22

if __name__ == '__main__':

    try:

        LETTERS = {
            "A":1,
            "B":2,
            "C":3,
            "D":4,
            "E":5,
            "F":6,
            "G":7,
            "H":8,
            "I":9,
            "J":10,
            "K":11,
            "L":12,
            "M":13,
            "N":14,
            "O":15,
            "P":16,
            "Q":17,
            "R":18,
            "S":19,
            "T":20,
            "U":21,
            "V":22,
            "W":23,
            "X":24,
            "Y":25,           
            "Z":26
        }

        def solve():
            stringData = ""
            fileHandler = open('project_euler_22_input.txt')
            for line in fileHandler:
                stringData += line

            result = 0

            names = stringData.split(",")
            print("Total Names: " + str(len(names))) # 5163
            # Must be sorted alphabetically first!
            names.sort()

            for x in range(0, len(names), 1):
                name = names[x].replace('"','')
                innerSum = 0

                for y in range(0, len(name), 1):
                    innerSum = innerSum + LETTERS[name[y]]

                score = innerSum * (x + 1)
                print("Current Name: " + name + " Inner Sum: " + str(innerSum) + " Name Number: " + str(x+1) + " Score: " + str(score))
                result = result + score

            return result

        print(solve()) # 871198282

    except Exception as ex:
        print('Exception: ' + str(ex))