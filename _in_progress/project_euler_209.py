# https://projecteuler.net/problem=209

if __name__ == '__main__':

    try:

        def xor(x, y):
            if (x == 0 and y == 0):
                return 0
            if (x == 0 and y == 1):
                return 1
            if (x == 1 and y == 0):
                return 1
            if (x == 1 and y == 1):
                return 0

        # Here since we're defining a meta-linguistic construct 
        # otherwise can just use and (... e.g. for clarity)
        def nd(x, y):
            if (x == 0 and y == 0):
                return 0
            if (x == 0 and y == 1):
                return 0
            if (x == 1 and y == 0):
                return 0
            if (x == 1 and y == 1):
                return 1       
       
       # 2^6 total distinct rows
       # Each of the 64 total distinct rows can also be assigned a 0 or a 1
       # Therefore 2^7 total arrays generated (64 distinct and mutually exclusive pairs)
        def generate_rows():
            rows = []
            # base_table_template = []

            for a in range(0,2,1):
                for b in range(0,2,1):
                    for c in range(0,2,1):
                        for d in range(0,2,1):
                            for e in range(0,2,1):
                                for f in range(0,2,1):
                                    # base_table_template.append([a,b,c,d,e,f])

                                    # This is the truth-assignment to the rest of the row
                                    # Truth in this form for 'nd'/'and' would be [[1, 1, 1], [0, 0, 0], [1, 0, 0], [0, 1, 0]]
                                    for g in range(0,2,1):
                                        rows.append([a,b,c,d,e,f,g])

            # print(str(base_table_template))
         
            return rows
        
        def compare(a, b):
            count = 0

            if not a[len(a) - 1] == b[len(b) - 1]:

                for x in range(0, len(a), 1):
                    if not a[x] == b[x]:
                        count+=1

                if count == 1:
                    for x in range(0, len(a), 1):
                        if not a[x] == b[x]:
                            print("invalid found " + str(a) + " " + str(b))
                            return False

            return True
        
        def solve():
            count = 0

            rows = generate_rows()

            print(str(len(rows)) + " Total Unique Rows Found")
            print(rows)

            left_match = []
            right_match = []

            for x in range(0, len(rows), 1):

                a = rows[x][0]
                b = rows[x][1]
                c = rows[x][2]
                d = rows[x][3]
                e = rows[x][4]
                f = rows[x][5]
                left_conjunct = rows[x][6]
                xx = xor(a, nd(b, c))

                for y in range(0, len(rows), 1):
                    y_a = rows[y][0]
                    y_b = rows[y][1]
                    y_c = rows[y][2]
                    y_d = rows[y][3]
                    y_e = rows[y][4]
                    y_f = rows[y][5]
                    right_conjunct = rows[y][6]

                    if b == y_a and c == y_b and d == y_c and e == y_d and f == y_e and xx == y_f:
                        if nd(left_conjunct, right_conjunct) == 0:
                            # relaxing the constraint here for not outright contradictory models but really counterintuitive ones:
                            #
                            #  [0, 1, 1, 1, 1, 1] 
                            #  [1, 1, 1, 1, 1, 1]
                            #
                            # e.g. the pair of rows above both resolve to false when it seems the first should be true and the second (or vice-versa)

                            #mututally_exl = True
                            #for z in range(0, len(rows[x]) - 1, 1):
                            #    if not rows[x][z] == rows[y][z]:
                            #        mututally_exl = False
                            #        break

                            #if not mututally_exl:
                                count += 1
                                print("Row match found: " + str(rows[x]) + " " + str(rows[y]))
                                left_match.append(rows[x])
                                right_match.append(rows[y])
            
            total_invalid = 0
            string_hashes = []
            string_hash_count = {}
            duplicates_count = 0

            for z in range(0, len(left_match), 1):
                if not compare(left_match[z], right_match[z]):
                    total_invalid += 1
                else:
                    string_hashes.append(str(left_match[z]))
                    string_hashes.append(str(right_match[z]))

                    key_a = str(left_match[z]) + " " + str(right_match[z])
                    val_a = string_hash_count.get(key_a)
                    if not val_a:
                        string_hash_count[key_a] = 1
                    else:
                        string_hash_count[key_a] = val_a + 1
                        print("Detected duplicate key_a: " + str(key_a))
                        duplicates_count += 1

                    key_b = str(right_match[z]) + " " + str(left_match[z])
                    val_b = string_hash_count.get(key_b)
                    if not val_b:
                        string_hash_count[key_b] = 1
                    else:
                        string_hash_count[key_b] = val_b + 1
                        print("Detected duplicate key_b: " + str(key_b))
                        duplicates_count += 1
            
            print("Total invalid combinations found: " + str(total_invalid))
            print("Valid string hashes found - should be even: " + str(len(string_hashes)))
            print("Duplicate string hashes found: " + str(duplicates_count))

            # 128 distinct rows can be generated.
            # Each 6 variable input truth-table has 2^6 rows (64 total).
            # Each match finds 2 rows and excludes 2 other options (since 64 / 128 total are mutually exclusive with the other option).
            # So, there are 2^6 rows - 2 remaining (62) and 124 remaining distinct combinations.
            # For each of the remaining 62 rows, there are 2 possible truth assignments.

            print("Matches found: " + str(count)) # 192
            valid_count = count - total_invalid - 3 # round(duplicates_count / 2) # 192 - 2 - 3 or 187
            print("Valid matches found: " + str(valid_count))
            table_rows_left = pow(2, 6) - 2
            print("Table rows remaining: " + str(table_rows_left)) # 62
            table_combos = pow(2, table_rows_left)
            print("Combinations per table found: " + str(table_combos)) # 1152921504606846976
            result = valid_count * table_combos
            print("Total combinations found: " + str(result)) # 862385285445921538048

            # Think the answer is strictly less than 862385285445921538048
            # Specifically strictly matches are less than 187 since some matches can be in the same table.
            return result

        solve()

    except Exception as ex:

        print('Exception: ' + str(ex))