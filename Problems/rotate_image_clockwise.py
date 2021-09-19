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
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
        for i in range(n):
            start = 0
            end = n - 1
            
            while start < end:
                temp = matrix[i][start]
                matrix[i][start] = matrix[i][end]
                matrix[i][end] = temp
                start += 1
                end -= 1
        
