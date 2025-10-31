# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        #turn tree into a graph (adj_list)
        #run bfs from the graph
        #return all nodes at level 2 of the bfs

        adj_list = defaultdict(list) #nodes -> adjacent neighbors
        ans = []
        queue = deque([root])

        def makeAdjList(root):

            if not root:
                return
            
            while queue:
                
                node = queue.popleft()
                
                if node.left:
                    adj_list[node.val].append(node.left.val)
                    adj_list[node.left.val].append(node.val)
                    queue.append(node.left)
                
                if node.right:
                    adj_list[node.val].append(node.right.val)
                    adj_list[node.right.val].append(node.val)
                    queue.append(node.right)
            
        makeAdjList(root)
    

        queue = deque([target.val])
        seen = {target.val}
        current_level = 0

        while queue:

            if current_level == k:
                return list(queue)
                

            level_size = len(queue)

            for _ in range(level_size):
                current_node = queue.popleft()

                for neighbor in adj_list[current_node]:

                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)

            current_level += 1
        
        return [] #no node distance k
