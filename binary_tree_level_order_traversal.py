from collections import deque


#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        tree_node_level = deque()
        tree_traversal = []
        if root:
            tree_node_level.append(root)
        while tree_node_level:
            next_tree_level = deque()
            level_traversal = []
            while tree_node_level:
                node = tree_node_level.popleft()
                level_traversal.append(node.val)
                if node.left:
                    next_tree_level.append(node.left)
                if node.right:
                    next_tree_level.append(node.right)
            tree_traversal.append(level_traversal)
            tree_node_level = next_tree_level
        return tree_traversal

            


t = TreeNode(
    val=3, 
    left=TreeNode(val=9, left=None, right=None), 
    right=TreeNode(
                    val=20, 
                    left=TreeNode(val=15, left=None, right=None), 
                    right=TreeNode(val=7, left=None, right=None)
                )
)
            
def main():
    s = Solution()
    print(s.levelOrder(t))


main()
        


