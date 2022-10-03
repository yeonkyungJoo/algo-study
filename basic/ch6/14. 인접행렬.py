import sys


# sys.stdin = open("../input.txt", "rt")

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        start, end, dist = map(int, input().split())
        arr[start-1][end-1] = dist

    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
