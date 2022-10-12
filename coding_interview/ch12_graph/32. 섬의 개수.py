if __name__ == "__main__":

    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]
    # grid = ['11110', '11010', '11000', '00000']
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def dfs(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            if grid[x][y] == 1:
                grid[x][y] = 0
                for k in range(4):
                    _x = x + dx[k]
                    _y = y + dy[k]
                    if 0 <= _x < len(grid) and 0 <= _y < len(grid[0]):
                        dfs(_x, _y)


    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)


