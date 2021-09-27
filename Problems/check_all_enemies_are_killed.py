def Kill_Enemy(s, row, col):
    i, j, x, y = 0, 0, 0, 0;
 
    # Loop to evaluate the Bomb
    for i in range(row):
        for j in range(col):
             
            # Check if this index is a bomb
            if (s[i][j] == 'B'):
 
                # Kill all enemies
                # in horizontal direction
                for x in range(row):
                    if (s[x][j] != 'B'):
                        s[x][j] = 'X';
 
                # Kill all enemies
                # in vertical direction
                for y in range(col):
                    if (s[i][y] != 'B'):
                        s[i][y] = 'X';
 
    # All bombs have been found
 
    # Check if any enemy is still present
    for i in range(row):
        for j in range(col):
 
            if (s[i][j] == 'E'):
 
                # Since an enemy is present
                # Return 0 denoting No as output
                return 0;
 
    # Since all enemies are killed
    # Return 1 denoting Yes as output
    return 1;
 
if __name__ == '__main__':
 
    # Get the input matrix
    s = [['X','X','E','X'],
        ['X','B','X','X'],
        ['X','E','X','X'],
        ['X','X','B','X']]
 
    # Calculate Rows and columns of the String
    row = len(s);
    col = len(s[0]);
 
    # Check if all enemies will be killed or not
    if (Kill_Enemy(s, row, col) == 1):
        print("Yes");
    else:
        print("No");
