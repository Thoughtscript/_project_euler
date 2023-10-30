# https://projecteuler.net/problem=51

import primes_to_5_mil as PRIMES

if __name__ == '__main__':

    try:
        def prime_map():
            primes = {}

            for x in range(0, len(PRIMES.primes), 1):
                primes[PRIMES.primes[x]] = True
            
            return primes

        PRIME_MAP = prime_map()
    
        def make_key(arr):
            string_result = ""

            for x in range(0, len(arr), 1):
                string_result = string_result + str(arr[x])

            return string_result

        def permute(original_arr):
            transfer_arr = original_arr
            heaps_results = {}

            def swap(end, begin):
                original = transfer_arr[begin]
                transfer_arr[begin] = transfer_arr[end]
                transfer_arr[end] = original

            def heaps_algorithm(n):
                if n == 1: 
                    key = make_key(transfer_arr)
                    heaps_results[key] = key
                    return
            
                for i in range(0, n, 1):
                    heaps_algorithm(n-1)
                    v = 0
                    if n % 2 == 0:
                        v = i
                    swap(n-1, v)

            heaps_algorithm(len(original_arr))
            return heaps_results
        
        def replace(num, replace_hm):

            max_len = len(str(num))
            heaps = replace_hm.get(max_len)
            heaps_vals = list(heaps.values())
            dedup = {}
            result = []

            for x in range(0, max_len, 1):
                for y in range(0, len(heaps_vals), 1):
                    curr = str(heaps_vals[y])
                    for z in range(0, x, 1):
                        str_result = ""

                        for w in range(0, max_len, 1):
                            if curr[w] == str(x) or curr[w] == str(z):
                                str_result += "-"
                            else:
                                str_result += str(num)[w]
                        
                        if dedup.get(str_result) is None:
                            result.append(str_result)
                            dedup[str_result] = str_result

            return result

        def fill(replacements, num, tried_map):
            for y in range(0, len(replacements), 1):
                if tried_map.get(replacements[y]) is None:
                    family = []
                    dedup_hm = {}
                    for x in range(0, 10, 1):
                        test_str = replacements[y].replace("-", str(x))
                        if not PRIME_MAP.get(int(test_str)) is None:
                            if dedup_hm.get(test_str) is None:
                                if not test_str == str(num) and not test_str[0] == "0":
                                    family.append(test_str)
                                    dedup_hm[test_str] = test_str
                    tried_map[replacements[y]] = replacements[y]
                    print("Family generated: " + str(family) + " for " + replacements[y])
                    if len(family) >= 8:
                        return family[0]
            return False
       
        def solve(mx_num):
            replace_hm = {}
            max_len = len(str(mx_num))
            tried_map = {}
            for x in range(0, max_len + 1, 1):
                arr = []
                for y in range(0, x, 1):
                    arr.append(y)
                replace_hm[x] = permute(arr)

            for curr_num in range(0, mx_num + 1, 1):
                replacements = replace(curr_num, replace_hm)
                test = fill(replacements, curr_num, tried_map)
                if not test == False:
                    print("Solution found: " + str(test))
                    return
                    
            print("No solution found!")

        solve(999999)

    except Exception as ex:

        print('Exception: ' + str(ex))