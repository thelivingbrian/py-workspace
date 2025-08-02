# LeetCode 110 - Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# Original solution w/ Devin 
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        def max_height(node, depth) -> int:
            if node is None: 
                return depth
            return max(max_height(node.left, depth+1), max_height(node.right, depth+1))

        if abs(max_height(root.left, 0) - max_height(root.right, 0)) > 1: # :(
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

# Cleaner logic 
class Solution1:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node) -> int:
            if node is None: 
                return 0 
            
            l, r = check_height(node.left), check_height(node.right)
            if l == -1 or r == -1:
                return -1
            
            if abs(l - r) > 1: 
                return -1

            return 1 + max(l, r)
        
        return check_height(root) != -1