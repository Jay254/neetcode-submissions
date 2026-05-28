"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(x0,y0,n):
            first_val = grid[x0][y0]
            uniform = True
            for i in range(x0, x0+n):
                for j in range(y0, y0+n):
                    if grid[i][j] != first_val:
                        uniform = False
                        break

                if not uniform:
                    break

            if uniform:
                return Node(bool(first_val), True, None, None, None, None)

            half = n // 2
            topL = build(x0,y0,half)
            topR = build(x0,y0+half,half)
            bottomL = build(x0+half,y0,half)
            bottomR = build(x0+half,y0+half, half)

            return Node(True, False, topL, topR, bottomL, bottomR)

        n = len(grid)
        return build(0,0,n)