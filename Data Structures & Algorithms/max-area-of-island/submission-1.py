class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        areas = []

        def bfs(r, c):
            area = 1
            q = deque([(r, c)])
            visited.add((r, c))
            while q:
                dr, dc = q.popleft()
                for (a, b) in [(0,-1), (0,1), (1,0), (-1, 0)]:
                    nr, nc = dr + a, dc + b
                    if (0 <= nr < rows and 0 <= nc < cols) and (grid[nr][nc] == 1) and ((nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        area += 1
            
            areas.append(area)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited :
                    bfs(r, c)
        if not areas:
            return 0
        return max(areas)

