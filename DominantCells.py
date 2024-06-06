def numCells(grid):
    def is_dominant(r, c):
        current_value = grid[r][c]
        rows = len(grid)
        cols = len(grid[0])
        
        # List of neighbor positions (8 directions)
        directions = [(-1, -1), (-1, 0), (-1, 1), 
                      (0, -1),          (0, 1), 
                      (1, -1), (1, 0), (1, 1)]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] >= current_value:
                    return False
        return True
    
    dominant_cells_count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if is_dominant(r, c):
                dominant_cells_count += 1
    
    return dominant_cells_count




def numCells2(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if all(grid[i][j] > grid[x][j] for x in range(len(grid))) \
               and all(grid[i][j] > grid[i][y] for y in range(len(grid[0]))):
                count += 1
    return count