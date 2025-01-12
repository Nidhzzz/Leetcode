class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()

        def rottenOrange(r,c):
            if (r<0 or r==rows or c<0 or c==cols or grid[r][c]==0 or (r,c) in visited):
                return
            elif (grid[r][c]==1):
                grid[r][c] = 2
            q.append([r,c])
            visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append([r,c])

        minute = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                rottenOrange(r+1,c)
                rottenOrange(r-1,c)
                rottenOrange(r,c+1)
                rottenOrange(r,c-1)
            minute += 1

        # for row in grid:
        #     if 1 in row:
        #         return -1
        if any(1 in row for row in grid):
            return -1
        return max(0, minute-1)