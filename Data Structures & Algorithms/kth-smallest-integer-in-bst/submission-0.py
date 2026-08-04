# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_list = []
        def preorder (root,sorted_list):

            if root:
            
                # print(root.val)
                preorder(root.left,sorted_list=sorted_list)
                sorted_list.append(root.val)
                preorder(root.right,sorted_list=sorted_list)

        preorder(root,sorted_list=sorted_list)
        return sorted_list[k - 1]
        