"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # Solution 1: level-order traversal (BFS) with queue
        # Time O(n) Space O(n)
        # if not root:
        #     return None
        # level = [root]
        # while level:
        #     for i in range(len(level) - 1):
        #         level[i].next = level[i + 1]
        #     level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        # return root
    
        # solution 2: next-pointer method
        # Time O(n) Space O(1)
        if not root:
            return None
        node = root
        while node.left:
            next_level_start = node.left
            while node:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                node = node.next
            node = next_level_start
        return root
                
            
            
            