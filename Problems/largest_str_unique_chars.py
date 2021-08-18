

def largerst_str(str_arr):
    N = len(str_arr)
    c = [0] * N

    # Index of string with maximum unique characters
    m =  0

    for j in range(N):
        # Array indicating any alphabet included or not
        character = [False] * 26

        # Count number of unique alphabet included or not included
        for k in range(len(str_arr[j])):
            x = ord(str_arr[j][k]) - ord("A")

            if ((str_arr[j][k] != " ") and (character[x] == False)):
                c[j] += 1
                character[x] = True

            # keep track of maximum number of alphabets
            if (c[j] > c[m]):
                m = j

    print(str_arr[m])


sa = ["BOBPQRSTUV", "A AB C JOHNSON","ANJALI", "ASKRIT", "ARMAN MALLIKPQRSTUVWXYZ"]
largerst_str(sa)
