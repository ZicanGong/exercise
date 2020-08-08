# https://leetcode-cn.com/problems/recover-binary-search-tree/submissions/
# 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        ldrList = []
        
        def inOrderTrav(node):
            if node.left:
                 inOrderTrav(node.left)
            ldrList.append(node.val)
            if node.right:
                inOrderTrav(node.right)
        
        inOrderTrav(root)

        errorIndecies = []
        
        for i in range(len(ldrList)-1):
            if ldrList[i] > ldrList[i+1]:
                errorIndecies.append(i)
                errorIndecies.append(i+1)

        firstNode = ldrList[errorIndecies[0]]
        secondNode = ldrList[errorIndecies.pop()]
        
        def switchNodes(node, firstNode, secondNode, switchCount=0):
            if node.val == firstNode:
                node.val = secondNode
                switchCount = switchCount + 1
            elif node.val == secondNode:
                node.val = firstNode
                switchCount = switchCount + 1
            if switchCount == 2:
                return
            if node.left:
                switchNodes(node.left, firstNode, secondNode, switchCount)
            if node.right:
                switchNodes(node.right, firstNode, secondNode, switchCount)
            
        switchNodes(root,firstNode,secondNode)
        return

#class Solution(object):
#     def recoverTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: None Do not return anything, modify root in-place instead.
#         """
#         switchList = [None,None,None]
        
#         def inOrderTrav(node):
#             if not node:
#                 return
#             inOrderTrav(node.left)
#             if switchList[0] and switchList[0].val > node.val:
#                 if not switchList[1]:
#                     switchList[1] = switchList[0]
#                 switchList[2] = node
#             switchList[0] = node
#             inOrderTrav(node.right)
        
#         inOrderTrav(root)
#         switchList[1].val, switchList[2].val = switchList[2].val, switchList[1].val
#         return

            
