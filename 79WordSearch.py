class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions =[(1,0),(-1,0),(0,1),(0,-1)]
        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if r<0 or r>=rows or c<0 or c>= cols or board[r][c] != word[i] or (r,c) in path:
                return False

            path.add((r,c))
            for x,y in directions:
                dr, dc = r+x, c+y
                if dfs(dr, dc, i+1):
                    return True

            path.remove((r,c))
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0) == True:
                    return True

        return False