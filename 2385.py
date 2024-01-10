# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution from lancertech6
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        # Turn the tree into a graph
        def dfs(node):
            if node is None:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)
        graph = defaultdict(list)
        dfs(root)
        visited = set()

        # A queue, containing the frontier of infection
        queue = deque([start])
        time = -1
        
        while queue:
            time +=1
            for _ in range(len(queue)):
                current = queue.popleft()
                visited.add(current)
                for i in graph[current]:
                    if i not in visited:
                        queue.append(i)
        return time
