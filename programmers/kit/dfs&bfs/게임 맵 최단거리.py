from collections import deque


def solution(maps):
    answer = -1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n, m = len(maps), len(maps[0])
    ch = [[0 for _ in range(m)] for _ in range(n)]

    queue = deque()
    queue.append((0, 0))
    ch[0][0] = 1
    while queue:
        x, y = queue.popleft()
        if x == (n - 1) and y == (m - 1):
            answer = ch[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if ch[nx][ny] == 0:
                    ch[nx][ny] = ch[x][y] + 1
                    queue.append((nx, ny))

    return answer