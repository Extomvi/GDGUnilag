"""Minimum Path Sum"""

def minPathSum(grid):
    ROWS, COLS = len(grid), len(grid[0])
    res = [[float("inf")] * (COLS + 1) for r in range(ROWS + 1)]
    #for r in range(ROWS+1):
    #    res.append([float("inf")]*(COLS+1))
    res[ROWS - 1][COLS] = 0

    for r in range(ROWS - 1, -1, -1):
        for c in range(COLS - 1, -1, -1):
            res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])

    return res[0][0]




if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6]]
    print(minPathSum(grid))