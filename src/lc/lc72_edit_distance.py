# Leetcode 72. Edit Distance
# https://leetcode.com/problems/edit-distance/

# First Solution - Levenshtein Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # - - H O R S E 
        # - 0 1 2 3 4 5
        # R 1 1 2 2 3 4 
        # O 2 2 1 2 3 4
        # S 3 3 2 2 2 3
        l1, l2 = len(word1), len(word2)
        matrix = [[i + j for j in range(l2+1)] for i in range(l1+1)]
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    minimum = min([matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]])
                    matrix[i][j] = 1 + minimum
        return matrix[-1][-1]