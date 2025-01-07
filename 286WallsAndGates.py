class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        visited = set()
        queue = collections.deque()
        
        def addRoom(r, c):
            if (r<0 or r == rows or c<0 or c == cols or (r,c) in visited or rooms[r][c] == -1):
                return
            queue.append([r,c])
            visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r,c))

        distance = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                
                rooms[r][c] = distance
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)

            distance += 1