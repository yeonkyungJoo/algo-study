if __name__ == "__main__":
    N = int(input())
    bricks = []
    for _ in range(N):
        s, h, w = map(int, input().split())
        bricks.append((s, w, h))

    bricks.sort(key=lambda x : (-x[0], -x[1], x[2]))
    dy = [bricks[i][2] for i in range(N)]
    for i in range(N):
        for j in range(i):
            if bricks[j][0] > bricks[i][0] and bricks[j][1] > bricks[i][1]:
                dy[i] = max(dy[j] + bricks[i][2], dy[i])
    print(max(dy))