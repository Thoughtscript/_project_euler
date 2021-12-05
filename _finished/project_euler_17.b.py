# https://projecteuler.net/problem=17

if __name__ == '__main__':

    try:

        def count_chars():

            fileHandler = open('generated_nums.txt')
            count = 0

            for line in fileHandler:
                line = line.replace(" ", "")
                line = line.replace("\n", "")
                count += len(line)
                print(line + " " + str(len(line)))

            print("Adding " + str(2673) + " for 'and's")
            return count + 2673

        print(count_chars()) # 21,124

    except Exception as ex:
        print('Exception: ' + str(ex))
