"""
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]


class Solution(object):
    def rotate(self, matrix):
        """
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        n = len(matrix)
        
        # Transpose the matrix
        for i in range(n):
            for j in range(n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            
            
        # Flip Horizantally
        for i in range(n):
            for j in range(n/2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j]
                matrix[i][n - 1 - j] = temp
                
        return matrix
        
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r-1):
                top, bottom = l, r
                
                # save the top left
                temp = matrix[top][l + i]
                
                # move left bottom to top left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # move bottom right to bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                # move top right to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]
                
                # move top left to top right
                matrix[top+i][r] = temp
                
            r -= 1
            l += 1
        
