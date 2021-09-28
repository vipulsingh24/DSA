def max_killed_enemies(area):
    if area == None or len(area) == 0 or len(area[0]) == 0:
        return 0
    
    m = len(area)
    n = len(area[0])
    max_enemies = 0
    row_count = 0
    col_count = [0] * n
    
    for i in range(m):
        for j in range(n):
            print("i, j: ", i, j)
            # start from first row, count the enemies in the current row between two walls
            # store it to avoid recompute
            if j == 0 or area[i][j-1] == "W":
                row_count = 0
                k = j
                while (k < n and area[i][k] != "W"):
                    if area[i][k] == "E":
                        row_count += 1
                    k += 1
            
            # start from column, count the enemies in the current col between two walls
            if i == 0 or area[i-1][j] == "W":
                col_count[j] = 0
                k = i
                while (k < m and area[k][j] != "W"):
                    if area[k][j] == "E":
                        col_count[j] += 1
                    k += 1                    
            
            # if this is a position to place the bomb, get the current max
            if area[i][j] == "0":
                max_enemies = max(max_enemies, row_count + col_count[j])
            
            print("Max enemies: ", max_enemies)
    
    return max_enemies


M = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
print(max_killed_enemies(M))  # 3
