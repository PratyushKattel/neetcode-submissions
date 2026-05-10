# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret_list = []
        if not root:
            return ret_list
        queue = [root]
        while queue:
            curr_list = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                curr_list.append(curr.val)
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            ret_list.append(curr_list[0])

        return ret_list
